import sys

from antlr4 import CommonTokenStream, InputStream, ParserRuleContext

from ohsome_filter_to_sql.OFLLexer import OFLLexer
from ohsome_filter_to_sql.OFLListener import OFLListener
from ohsome_filter_to_sql.OFLParser import OFLParser


class OhsomeFilterToSql(OFLListener):
    pass


def main(filter: str):
    build_tree(filter)


def build_tree(filter) -> ParserRuleContext:
    """Build a antlr4 parse tree."""
    input_stream = InputStream(filter)
    lexer = OFLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = OFLParser(stream)
    tree = parser.root()
    return tree


if __name__ == "__main__":
    main(sys.argv[1])
