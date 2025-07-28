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
        if ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == ("(") and ctx.getChild(2).getText() == ")":
                expression = self.stack.pop()
                self.stack.append("(" + expression + ")")
            else:
                right = self.stack.pop()
                left = self.stack.pop()
                operator = ctx.getChild(1).getText()
                self.stack.append(left + " " + operator.toUpperCase() + " " + right)

    def exitString(self, ctx):  # noqa
        self.stack.append(unescape(ctx.getChild(0).getText()))

    def exitTagMatch(self, ctx):  # noqa
        value = self.stack.pop()
        key = self.stack.pop()
        self.stack.append(key + " = " + value)

    def exitTagWildcardMatch(self, ctx):  # noqa
        key = self.stack.pop()
        self.stack.append(key + " IS NOT NULL")

    def exitTagNotMatch(self, ctx):  # noqa
        value = self.stack.pop()
        key = self.stack.pop()
        self.stack.append(key + " != " + value)

    def exitTagNotWildcardMatch(self, ctx):  # noqa
        key = self.stack.pop()
        self.stack.append(key + " IS NULL")

    def exitTagListMatch(self, ctx):  # noqa
        # TODO: does not work as expected
        values = parse_list(ctx)
        key = self.stack.pop()
        self.stack.append(key + f" IN ({''.join(values)})")


def unescape(string: str):
    return string.replace('"', "")


def parse_list(ctx):
    values = []
    children = list(ctx.getChildren())
    #  for i in range(3, len(children), 2):
    for child in children[3:-1]:
        values.append(child.getText())
    return values


def main(filter: str):
    listener = OFLToSql()
    tree = build_tree(filter)
    translation = walk_tree(tree, listener).stack
    return " ".join(translation)


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
