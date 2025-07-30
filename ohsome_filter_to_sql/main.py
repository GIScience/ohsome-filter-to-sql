import sys
from collections import deque

from antlr4 import CommonTokenStream, InputStream, ParserRuleContext, ParseTreeWalker

from ohsome_filter_to_sql.OFLLexer import OFLLexer
from ohsome_filter_to_sql.OFLListener import OFLListener
from ohsome_filter_to_sql.OFLParser import OFLParser


class OFLToSql(OFLListener):
    def __init__(self):
        self.stack: deque = deque()

    def exitExpression(self, ctx):  # noqa
        """Handle expression compositions.

        '(' expression ')'
        NOT expression
        expression AND expression
        expression OR expression
        """
        if ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == ("(") and ctx.getChild(2).getText() == ")":
                expression = self.stack.pop()
                self.stack.append("(" + expression + ")")
            else:
                right = self.stack.pop()
                left = self.stack.pop()
                operator = ctx.getChild(1).getText().upper()  # AND, OR, NOT
                self.stack.append(f"{left} {operator} {right}")

    def exitString(self, ctx):  # noqa
        self.stack.append(unescape(ctx.getChild(0).getText()))

    def exitTagMatch(self, ctx):  # noqa
        value = self.stack.pop()
        key = self.stack.pop()
        self.stack.append(f"tags->>'{key}' = '{value}'")

    def exitTagWildcardMatch(self, ctx):  # noqa
        key = self.stack.pop()
        self.stack.append(f"tags->>'{key}' IS NOT NULL")

    def exitTagNotMatch(self, ctx):  # noqa
        value = self.stack.pop()
        key = self.stack.pop()
        self.stack.append(f"tags->>'{key}' != '{value}'")

    def exitTagNotWildcardMatch(self, ctx):  # noqa
        key = self.stack.pop()
        self.stack.append(f"tags->>'{key}' IS NULL")

    def exitTagListMatch(self, ctx):  # noqa
        # TODO: does not work as expected
        values = []
        children = list(child.getText() for child in ctx.getChildren())
        # skip first part denoting "key in (" as well as last part closing list with ")"
        for child in children[3:-1]:
            # skip comma in list in between brackets
            if child == ",":
                continue
            # remove STRING from stack wich are part of TagListMatch
            self.stack.pop()
            values.append(child)
        key = self.stack.pop()
        values_as_string = "', '".join(values)
        self.stack.append(f"tags->>'{key}' IN ('{values_as_string}')")

    def exitTypeMatch(self, ctx):  # noqa
        type_ = ctx.getChild(2).getText().upper()
        self.stack.append(f"osmType = '{type_}'")

    def exitIdMatch(self, ctx):  # noqa
        id = ctx.getChild(2).getText()
        self.stack.append(f"osmId = '{id}'")

    def exitTypeIdMatch(self, ctx):  # noqa
        type_, id = ctx.getChild(2).getText().split("/")
        self.stack.append(f"osmType = '{type_}' AND osmId = '{id}'")

    def exitIdRangeMatch(self, ctx):  # noqa
        child = ctx.getChild(3).getText()
        lower_bound, upper_bound = child.split("..")
        if lower_bound and upper_bound:
            self.stack.append(f"osmID >= '{lower_bound}' AND osmID <= '{upper_bound}'")
        elif lower_bound:
            self.stack.append(f"osmID >= '{lower_bound}'")
        elif upper_bound:
            self.stack.append(f"osmID <= '{upper_bound}'")


def unescape(string: str):
    return string.replace('"', "")


def main(filter: str):
    listener = OFLToSql()
    tree = build_tree(filter)
    translation = walk_tree(tree, listener).stack
    return " ".join(translation)


def cli():
    print(main(input()))


def build_tree(filter: str) -> ParserRuleContext:
    """Build a antlr4 parse tree.

    https://github.com/antlr/antlr4/blob/master/doc/listeners.md
    """
    input_stream = InputStream(filter)
    lexer = OFLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = OFLParser(stream)
    tree = parser.root()
    return tree


def walk_tree(tree: ParserRuleContext, listener: OFLToSql) -> OFLToSql:
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener


if __name__ == "__main__":
    main(sys.argv[1])
