import sys
from enum import Enum
from typing import Annotated

from antlr4 import CommonTokenStream, InputStream, ParserRuleContext, ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener
from pydantic import AfterValidator, Field, validate_call
from typing_extensions import TypeAliasType

from ohsome_filter_to_sql.OFLCLexer import OFLCLexer
from ohsome_filter_to_sql.OFLCParser import OFLCParser
from ohsome_filter_to_sql.OFLLexer import OFLLexer
from ohsome_filter_to_sql.OFLParser import OFLParser
from ohsome_filter_to_sql.ohsome_changeset_filter import OFLCToSql
from ohsome_filter_to_sql.ohsome_filter import OFLToSql


class FilterType(Enum):
    OHSOME_FILTER = 1
    CHANGESET_FILTER = 2


def validate_filter(
    filter_: str,
    filter_type: FilterType = FilterType.OHSOME_FILTER,
) -> str:
    match filter_type:
        case FilterType.OHSOME_FILTER:
            listener = OFLToSql()
            tree = build_tree(filter_)
        case FilterType.CHANGESET_FILTER:
            listener = OFLCToSql()
            tree = build_tree(filter_)
    walk_tree(tree, listener)
    return filter_


class ParserValueError(ValueError):
    pass


class LexerValueError(ValueError):
    pass


class ParserErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # message is based on antlr4 ConsoleErrorListener
        raise ParserValueError("line " + str(line) + ":" + str(column) + " " + msg)


class LexerErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise LexerValueError("line " + str(line) + ":" + str(column) + " " + msg)


def build_tree(
    filter_: str,
    filter_type: FilterType = FilterType.OHSOME_FILTER,
) -> ParserRuleContext:
    """Build a antlr4 parse tree.

    https://github.com/antlr/antlr4/blob/master/doc/listeners.md
    """
    input_stream = InputStream(filter_)
    match filter_type:
        case FilterType.OHSOME_FILTER:
            lexer = OFLLexer(input_stream)
        case FilterType.CHANGESET_FILTER:
            lexer = OFLCLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(LexerErrorListener())
    stream = CommonTokenStream(lexer)
    match filter_type:
        case FilterType.OHSOME_FILTER:
            parser = OFLParser(stream)
        case FilterType.CHANGESET_FILTER:
            parser = OFLCParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ParserErrorListener())
    tree = parser.root()
    return tree


def walk_tree[T: OFLToSql | OFLCToSql](tree: ParserRuleContext, listener: T) -> T:
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener


@validate_call
def ohsome_filter_to_sql(
    filter_: Annotated[str, Field(min_length=1)],
    args_shift: Annotated[int, Field(ge=0, default=0)] = 0,
    filter_type: FilterType = FilterType.OHSOME_FILTER,
) -> tuple[str, tuple[str | int | float | tuple, ...]]:
    """Translate ohsome filter into a SQL WHERE clause for ohsome DB.

    Args:
        filter_: Ohsome filter
        args_shift: Integer by which to shift numbered query arguments: $n + arg_shift

    Returns:
        The SQL WHERE clause in native PostgreSQL syntax for query arguments: $n.
        The query arguments.
    """
    if filter_ == "*":
        return ("1=1", tuple())
    match filter_type:
        case FilterType.OHSOME_FILTER:
            listener = OFLToSql(args_shift)
        case FilterType.CHANGESET_FILTER:
            listener = OFLCToSql(args_shift)
    tree = build_tree(filter_, filter_type)
    result = walk_tree(tree, listener)
    query = " ".join(result.stack)
    query_args = tuple(result.args)
    return (query, query_args)


def cli():
    print(ohsome_filter_to_sql(input()))


OhsomeFilter = TypeAliasType(
    "OhsomeFilter",
    Annotated[str, AfterValidator(validate_filter)],
)


if __name__ == "__main__":
    ohsome_filter_to_sql(sys.argv[1])
