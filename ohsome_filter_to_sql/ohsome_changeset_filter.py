import json
from collections import deque

from antlr4 import ParserRuleContext

from ohsome_filter_to_sql.OFLCListener import OFLCListener
from ohsome_filter_to_sql.ohsome_filter import InvalidRangeError, unescape


class OFLCToSql(OFLCListener):
    def __init__(self, args_shift: int = 0):
        self.stack: deque[str] = deque()
        self.args: deque[str | int | float | tuple] = deque()
        self.args_shift: int = args_shift

    @property
    def args_len(self) -> int:
        return len(self.args) + self.args_shift

    def exitString(self, ctx: ParserRuleContext):
        if ctx.getChildCount() == 1:
            self.stack.append(unescape(ctx.getChild(0).getText()))
        else:
            result = ""
            for child in ctx.getChildren():
                result += child.getText()
            self.stack.append(result)

    def exitRange_int(self, ctx):
        """Remove range brackets."""
        self.stack.append(ctx.getText().strip()[1:-1].strip())

    def exitRange_dec(self, ctx):
        """Remove range brackets."""
        self.stack.append(ctx.getText().strip()[1:-1].strip())

    # --- methods are sorted in the same order as rules in OFL.g4
    #
    def exitExpression(self, ctx: ParserRuleContext):
        """Handle expression compositions: (), NOT, AND, OR"""
        if ctx.getChildCount() == 3:
            if (
                ctx.getChild(0).getText().strip() == "("
                and ctx.getChild(2).getText().strip() == ")"
            ):
                expression = self.stack.pop()
                self.stack.append("(" + expression + ")")
            else:
                right = self.stack.pop()
                left = self.stack.pop()
                operator = ctx.getChild(1).getText().strip().upper()  # AND, OR
                self.stack.append(f"{left} {operator} {right}")
        elif ctx.getChildCount() == 2:
            operator = ctx.getChild(0).getText().strip().upper()  # NOT
            self.stack.append(f"{operator} {self.stack.pop()}")

    # ---
    #
    def exitTagMatch(self, ctx: ParserRuleContext):
        value = self.stack.pop()
        key = self.stack.pop()
        j = json.dumps({key: value})
        # @> Does the first JSON value contain the second?
        self.args.append(j)
        self.stack.append(f"changesets.tags @> ${self.args_len}")

    def exitTagValuePatternMatch(self, ctx):
        value = (
            self.stack.pop().replace("%", "\\%").replace("_", "\\_").replace("'", "''")
        )
        key = self.stack.pop().replace("'", "''")

        value_child = ctx.getChild(2)
        if value_child.getChild(0).getText() == "*":
            value = "%" + value

        if value_child.getChild(value_child.getChildCount() - 1).getText() == "*":
            value = value + "%"

        self.args.append(key)
        self.args.append(value)
        self.stack.append(
            f"((changesets.tags->>${self.args_len - 1}) IS NOT NULL "
            f"AND (changesets.tags->>${self.args_len - 1}) LIKE ${self.args_len})"
        )

    def exitTagWildcardMatch(self, ctx: ParserRuleContext):
        key = self.stack.pop()
        self.args.append(key)
        self.stack.append(f"changesets.tags ? ${self.args_len}")

    def exitTagNotMatch(self, ctx: ParserRuleContext):
        value = self.stack.pop()
        key = self.stack.pop()
        j = json.dumps({key: value})
        self.args.append(j)
        self.stack.append(f"NOT changesets.tags @> ${self.args_len}")

    def exitTagNotWildcardMatch(self, ctx: ParserRuleContext):
        key = self.stack.pop()
        self.args.append(key)
        self.stack.append(f"NOT changesets.tags ? ${self.args_len}")

    def exitTagListMatch(self, ctx: ParserRuleContext):
        values = []
        children = [child.getText() for child in ctx.getChildren()]
        # skip first part denoting "key in (" as well as last part closing list with ")"
        # and skip commas in list in between brackets
        for child in children[3:-1:2]:
            # remove STRING from stack wich are part of *ListMatch
            self.stack.pop()
            values.append('"' + unescape(child) + '"')
        key = self.stack.pop()
        self.args.append(key)
        self.args.append(tuple(values))
        self.stack.append(
            f"((changesets.tags->${self.args_len - 1}) IS NOT NULL "
            f"AND (changesets.tags->${self.args_len - 1}) = ANY(${self.args_len}))"
        )

    # ---
    #
    def exitIdMatch(self, ctx: ParserRuleContext):
        id_ = ctx.getChild(2).getText()
        self.args.append(int(id_))
        self.stack.append(f"changesets.id = ${self.args_len}")

    def exitIdRangeMatch(self, ctx: ParserRuleContext):
        range_ = self.stack.pop()
        lower_bound, upper_bound = [
            int(n.strip()) if n else None for n in range_.split("..")
        ]
        if lower_bound and upper_bound:
            if lower_bound > upper_bound:
                raise InvalidRangeError(upper_bound, lower_bound)
            self.args.append(lower_bound)
            self.args.append(upper_bound)
            self.stack.append(
                f"(changesets.id >= ${self.args_len - 1} "
                f"AND changesets.id <= ${self.args_len})"
            )
        elif lower_bound:
            self.args.append(lower_bound)
            self.stack.append(f"changesets.id >= ${self.args_len}")
        elif upper_bound:
            self.args.append(upper_bound)
            self.stack.append(f"changesets.id <= ${self.args_len}")

    def exitIdListMatch(self, ctx: ParserRuleContext):
        # differs from TagListMatch insofar that no STRING needs to be popped from stack
        values = []
        children = [child.getText() for child in ctx.getChildren()]
        # skip first part denoting "id:(" as well as last part closing list with ")"
        # and skip commas in list in between brackets
        values = list(children[3:-1:2])
        self.args.append(tuple([int(v) for v in values]))
        self.stack.append(f"changesets.id = ANY(${self.args_len})")

    # ---
    #
    def exitHashtagMatch(self, ctx: ParserRuleContext):
        hashtag = ctx.getChild(2).getText()
        self.args.append(hashtag)
        self.stack.append(
            f"${self.args_len} = ANY(STRING_TO_ARRAY(c.tags->hashtags, ';'))"
        )
