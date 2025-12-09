import json
import sys
from collections import deque

from antlr4 import CommonTokenStream, InputStream, ParserRuleContext, ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener

from ohsome_filter_to_sql.OFLLexer import OFLLexer
from ohsome_filter_to_sql.OFLListener import OFLListener
from ohsome_filter_to_sql.OFLParser import OFLParser


class ParserValueError(ValueError):
    pass


class LexerValueError(ValueError):
    pass


class InvalidRangeError(ValueError):
    def __init__(self, lower_bound, upper_bound):
        super().__init__(
            "Upper bound is smaller the then lower bound. "
            f"Try swapping bounds: ({lower_bound}..{upper_bound})"
        )


class OFLParserErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # message is based on antlr4 ConsoleErrorListener
        raise ParserValueError("line " + str(line) + ":" + str(column) + " " + msg)


class OFLLexerErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise LexerValueError("line " + str(line) + ":" + str(column) + " " + msg)


class OFLToSql(OFLListener):
    def __init__(self):
        self.stack: deque[str] = deque()
        self.args: deque[str | int | float | tuple] = deque()

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
    def exitHashtagMatch(self, ctx: ParserRuleContext):
        hashtag = self.stack.pop()
        self.args.append(hashtag)
        self.stack.append(f"${len(self.args)} = any(changeset_hashtags) ")

    def exitHashtagWildcardMatch(self, ctx: ParserRuleContext):
        # TODO
        raise NotImplementedError()

    def exitHashtagListMatch(self, ctx: ParserRuleContext):
        values = []
        children = list(child.getText() for child in ctx.getChildren())
        # skip first part denoting "hashtag:(" and last part closing list with ")"
        # and skip commas in list in between brackets (every second child)
        for child in children[3:-1:2]:
            # remove STRING from stack
            self.stack.pop()
            values.append(child)
        values_as_string = "array['" + "', '".join(values) + "']"
        # anyarray && anyarray → boolean (Do the arrays overlap?)
        self.args.append(values_as_string)
        self.stack.append(f"${len(self.args)} && changeset_hashtags")

    # ---
    #
    def exitTagMatch(self, ctx: ParserRuleContext):
        value = self.stack.pop()
        key = self.stack.pop()
        j = json.dumps({key: value})
        # @> Does the first JSON value contain the second?
        self.args.append(j)
        self.stack.append(f"tags @> ${len(self.args)}")

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
        self.stack.append(f"tags ->> ${len(self.args) - 1} LIKE ${len(self.args)}")

    def exitTagWildcardMatch(self, ctx: ParserRuleContext):
        key = self.stack.pop()
        self.args.append(key)
        self.stack.append(f"tags ? ${len(self.args)}")

    def exitTagNotMatch(self, ctx: ParserRuleContext):
        value = self.stack.pop()
        key = self.stack.pop()
        j = json.dumps({key: value})
        self.args.append(j)
        self.stack.append(f"NOT tags @> ${len(self.args)}")

    def exitTagNotWildcardMatch(self, ctx: ParserRuleContext):
        key = self.stack.pop()
        self.args.append(key)
        self.stack.append(f"NOT tags ? ${len(self.args)}")

    def exitTagListMatch(self, ctx: ParserRuleContext):
        values = []
        children = list(child.getText() for child in ctx.getChildren())
        # skip first part denoting "key in (" as well as last part closing list with ")"
        # and skip commas in list in between brackets
        for child in children[3:-1:2]:
            # remove STRING from stack wich are part of *ListMatch
            self.stack.pop()
            values.append('"' + unescape(child) + '"')
        key = self.stack.pop()
        self.args.append(key)
        self.args.append(tuple(values))
        self.stack.append(f"(tags -> ${len(self.args) - 1}) = ANY(${len(self.args)})")

    # ---
    #
    def exitTypeMatch(self, ctx: ParserRuleContext):
        type_ = ctx.getChild(2).getText()  # NODE, WAY, RELATION
        self.args.append(type_)
        self.stack.append(f"osm_type = ${len(self.args)}")

    def exitIdMatch(self, ctx: ParserRuleContext):
        id = ctx.getChild(2).getText()
        self.args.append(int(id))
        self.stack.append(f"osm_id = ${len(self.args)}")

    def exitTypeIdMatch(self, ctx: ParserRuleContext):
        type_, id = ctx.getChild(2).getText().split("/")
        self.args.append(type_)
        self.args.append(int(id))
        self.stack.append(
            f"(osm_type = ${len(self.args) - 1} AND osm_id = ${len(self.args)})"
        )

    def exitIdRangeMatch(self, ctx: ParserRuleContext):
        range = self.stack.pop()
        lower_bound, upper_bound = [
            int(n.strip()) if n else None for n in range.split("..")
        ]
        if lower_bound and upper_bound:
            if lower_bound > upper_bound:
                raise InvalidRangeError(upper_bound, lower_bound)
            self.args.append(lower_bound)
            self.args.append(upper_bound)
            self.stack.append(
                f"(osm_id >= ${len(self.args) - 1} AND osm_id <= ${len(self.args)})"
            )
        elif lower_bound:
            self.args.append(lower_bound)
            self.stack.append(f"osm_id >= ${len(self.args)}")
        elif upper_bound:
            self.args.append(upper_bound)
            self.stack.append(f"osm_id <= ${len(self.args)}")

    def exitIdListMatch(self, ctx: ParserRuleContext):
        # differs from TagListMatch insofar that no STRING needs to be popped from stack
        values = []
        children = list(child.getText() for child in ctx.getChildren())
        # skip first part denoting "id:(" as well as last part closing list with ")"
        # and skip commas in list in between brackets
        values = list(children[3:-1:2])
        self.args.append(tuple([int(v) for v in values]))
        self.stack.append(f"osm_id = ANY(${len(self.args)})")

    def exitTypeIdListMatch(self, ctx: ParserRuleContext):
        # TODO
        values = []
        children = list(child.getText() for child in ctx.getChildren())
        # skip first part denoting "id:(" as well as last part closing list with ")"
        # and skip commas in list in between brackets
        for child in children[3:-1:2]:
            type_, id = child.split("/")
            self.args.append(int(id))
            self.args.append(type_)
            values.append(
                f"(osm_id = ${len(self.args) - 1} AND osm_type = ${len(self.args)})"
            )
        if len(values) > 1:
            self.stack.append("(" + " OR ".join(values) + ")")
        else:
            self.stack.append(" OR ".join(values))

    # ---
    #
    def exitGeometryMatch(self, ctx: ParserRuleContext):
        geom_type = ctx.getChild(2).getText()
        match geom_type:
            case "point":
                self.stack.append("(status_geom_type).geom_type = 'Point'")
            case "line":
                self.stack.append("(status_geom_type).geom_type = 'LineString'")
            case "polygon":
                self.stack.append(
                    "((status_geom_type).geom_type = 'Polygon' "
                    + "OR (status_geom_type).geom_type = 'MultiPolygon')"
                )
            case "other":
                self.stack.append("(status_geom_type).geom_type = 'GeometryCollection'")

    def exitAreaRangeMatch(self, ctx: ParserRuleContext):
        range = self.stack.pop()
        lower_bound, upper_bound = [
            float(n.strip()) if n else None for n in range.split("..")
        ]
        if lower_bound and upper_bound:
            if lower_bound > upper_bound:
                raise InvalidRangeError(upper_bound, lower_bound)
            self.args.append(lower_bound)
            self.args.append(upper_bound)
            self.stack.append(
                f"(area >= ${len(self.args) - 1} AND area <= ${len(self.args)})"
            )
        elif lower_bound:
            self.args.append(lower_bound)
            self.stack.append(f"area >= ${len(self.args)}")
        elif upper_bound:
            self.args.append(upper_bound)
            self.stack.append(f"area <= ${len(self.args)}")

    def exitLengthRangeMatch(self, ctx: ParserRuleContext):
        range = self.stack.pop()
        lower_bound, upper_bound = [
            float(n.strip()) if n else None for n in range.split("..")
        ]
        if lower_bound and upper_bound:
            if lower_bound > upper_bound:
                raise InvalidRangeError(upper_bound, lower_bound)
            self.args.append(lower_bound)
            self.args.append(upper_bound)
            self.stack.append(
                f"(length >= ${len(self.args) - 1} AND length <= ${len(self.args)})"
            )
        elif lower_bound:
            self.args.append(lower_bound)
            self.stack.append(f"length >= ${len(self.args)}")
        elif upper_bound:
            self.args.append(upper_bound)
            self.stack.append(f"length <= ${len(self.args)}")

    def exitGeometryVerticesRangeMatch(self, ctx: ParserRuleContext):
        # TODO
        raise NotImplementedError()

    def exitGeometryOutersMatch(self, ctx: ParserRuleContext):
        # TODO
        raise NotImplementedError()

    def exitGeometryOutersRangeMatch(self, ctx: ParserRuleContext):
        # TODO
        raise NotImplementedError()

    def exitGeometryInnersMatch(self, ctx: ParserRuleContext):
        # TODO
        raise NotImplementedError()

    def exitGeometryInnersRangeMatch(self, ctx: ParserRuleContext):
        # TODO
        raise NotImplementedError()

    # ---
    #
    def exitChangesetMatch(self, ctx: ParserRuleContext):
        id = int(ctx.getChild(2).getText())
        self.args.append(id)
        self.stack.append(f"changeset_id = ${len(self.args)}")

    def exitChangesetListMatch(self, ctx: ParserRuleContext):
        children = list(child.getText() for child in ctx.getChildren())
        # skip first part denoting "id:(" as well as last part closing list with ")"
        # and skip commas in list in between brackets
        self.args.append(tuple([int(i) for i in children[3:-1:2]]))
        self.stack.append(f"changeset_id = ANY(${len(self.args)})")

    def exitChangesetRangeMatch(self, ctx: ParserRuleContext):
        range = self.stack.pop()
        lower_bound, upper_bound = [
            int(n.strip()) if n else None for n in range.split("..")
        ]
        if lower_bound and upper_bound:
            self.args.append(lower_bound)
            self.args.append(lower_bound)
            self.stack.append(
                f"(changeset_id >= ${len(self.args) - 1} "
                f"AND changeset_id <= ${len(self.args)})"
            )
        elif lower_bound:
            self.args.append(lower_bound)
            self.stack.append(f"changeset_id >= ${len(self.args)}")
        elif upper_bound:
            self.args.append(upper_bound)
            self.stack.append(f"changeset_id <= ${len(self.args)}")

    def exitChangesetCreatedByMatch(self, ctx: ParserRuleContext):
        editor = self.stack.pop()
        j = json.dumps({"created_by": editor})
        self.args.append(j)
        self.stack.append(f"changeset_tags @> ${len(self.args)}")


def unescape(string: str):
    if string[0] == '"':
        string = string[1:-1]
        # fmt: off
        string = string.replace("\\\"", "\"") # noqa: Q003
        # fmt: on
        string = string.replace("\\\\", "\\")
        string = string.replace("\\\r", "\r")
        string = string.replace("\\\n", "\n")
    return string


def ohsome_filter_to_sql(
    filter: str,
) -> tuple[str, tuple[str | int | float | tuple, ...]]:
    listener = OFLToSql()
    tree = build_tree(filter)
    result = walk_tree(tree, listener)
    query = " ".join(result.stack)
    query_args = tuple(result.args)
    return (query, query_args)


def cli():
    print(ohsome_filter_to_sql(input()))


def build_tree(filter: str) -> ParserRuleContext:
    """Build a antlr4 parse tree.

    https://github.com/antlr/antlr4/blob/master/doc/listeners.md
    """
    input_stream = InputStream(filter)
    lexer = OFLLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(OFLLexerErrorListener())
    stream = CommonTokenStream(lexer)
    parser = OFLParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(OFLParserErrorListener())
    tree = parser.root()
    return tree


def walk_tree(tree: ParserRuleContext, listener: OFLToSql) -> OFLToSql:
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener


if __name__ == "__main__":
    ohsome_filter_to_sql(sys.argv[1])
