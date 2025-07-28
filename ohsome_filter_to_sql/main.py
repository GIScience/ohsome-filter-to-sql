import sys
from collections import deque

from antlr4 import CommonTokenStream, InputStream, ParserRuleContext, ParseTreeWalker

from ohsome_filter_to_sql.OFLLexer import OFLLexer
from ohsome_filter_to_sql.OFLListener import OFLListener
from ohsome_filter_to_sql.OFLParser import OFLParser


class OFLToSql(OFLListener):
    def __init__(self):
        self.stack: deque = deque()

    def exitString(self, ctx):  # noqa: N802
        self.stack.append(ctx.getChild(0).getText())

    def exitTagMatch(self, ctx):  # noqa: N802
        value = self.stack.pop()
        key = self.stack.pop()
        self.stack.append(key + " = " + value)


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
