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


class OFLParserErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # message is based on antlr4 ConsoleErrorListener
        raise ParserValueError("line " + str(line) + ":" + str(column) + " " + msg)


class OFLLexerErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise LexerValueError("line " + str(line) + ":" + str(column) + " " + msg)


class OFLToSql(OFLListener):
    def __init__(self):
        self.stack: deque = deque()

    def exitString(self, ctx: ParserRuleContext):
        if ctx.getChildCount() == 1:
            self.stack.append(unescape(ctx.getChild(0).getText()))
        else:
            result = ""
            for child in ctx.getChildren():
                result += child.getText()
            self.stack.append(result)

    # --- methods are sorted in the same order as rules in OFL.g4
    #
    def exitExpression(self, ctx: ParserRuleContext):
        """Handle expression compositions: (), NOT, AND, OR"""
        if ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == ("(") and ctx.getChild(2).getText() == ")":
                expression = self.stack.pop()
                self.stack.append("(" + expression + ")")
            else:
                right = self.stack.pop()
                left = self.stack.pop()
                operator = ctx.getChild(1).getText().upper()  # AND, OR
                self.stack.append(f"{left} {operator} {right}")
        elif ctx.getChildCount() == 2:
            operator = ctx.getChild(0).getText().upper()  # NOT
            self.stack.append(f"{operator} {self.stack.pop()}")

    # ---
    #
    def exitHashtagMatch(self, ctx: ParserRuleContext):
        hashtag = self.stack.pop()
        self.stack.append(f"'{hashtag}' = any(changeset_hashtags) ")

    def exitHashtagWildcardMatch(self, ctx: ParserRuleContext):
        # TODO
        pass

    def exitHashtagListMatch(self, ctx: ParserRuleContext):
        values = []
        children = list(child.getText() for child in ctx.getChildren())
        # skip first part denoting "hashtag:(" and last part closing list with ")"
        for child in children[3:-1]:
            # skip comma in list in between brackets
            if child == ",":
                continue
            # remove STRING from stack
            self.stack.pop()
            values.append(child)
        values_as_string = "array['" + "', '".join(values) + "']"
        # anyarray && anyarray → boolean (Do the arrays overlap?)
        self.stack.append(f"{values_as_string} && changeset_hashtags")

    # ---
    #
    def exitTagMatch(self, ctx: ParserRuleContext):
        value = self.stack.pop()
        key = self.stack.pop()

        j = json.dumps({key: value})
        # @> Does the first JSON value contain the second?
        self.stack.append(f"tags @> '{j}'")

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

        self.stack.append(f"tags ->> '{key}' LIKE '{value}'")

    def exitTagWildcardMatch(self, ctx: ParserRuleContext):
        key = self.stack.pop()
        self.stack.append(f"tags ? '{key}'")

    def exitTagNotMatch(self, ctx: ParserRuleContext):
        value = self.stack.pop()
        key = self.stack.pop()
        j = json.dumps({key: value})
        self.stack.append(f"NOT tags @> '{j}'")

    def exitTagNotWildcardMatch(self, ctx: ParserRuleContext):
        key = self.stack.pop()
        self.stack.append(f"NOT tags ? '{key}'")

    def exitTagListMatch(self, ctx: ParserRuleContext):
        values = []
        children = list(child.getText() for child in ctx.getChildren())
        # skip first part denoting "key in (" as well as last part closing list with ")"
        for child in children[3:-1]:
            # skip comma in list in between brackets
            if child == ",":
                continue
            # remove STRING from stack wich are part of *ListMatch
            self.stack.pop()
            values.append(unescape(child))
        values_as_string = "\"', '\"".join(values)
        key = self.stack.pop()
        self.stack.append(f"tags -> '{key}' IN ('\"{values_as_string}\"')")

    # ---
    #
    def exitTypeMatch(self, ctx: ParserRuleContext):
        type_ = ctx.getChild(2).getText()  # NODE, WAY, RELATION
        self.stack.append(f"osm_type = '{type_}'")

    def exitIdMatch(self, ctx: ParserRuleContext):
        id = ctx.getChild(2).getText()
        self.stack.append(f"osm_id = {id}")

    def exitTypeIdMatch(self, ctx: ParserRuleContext):
        type_, id = ctx.getChild(2).getText().split("/")
        self.stack.append(f"(osm_type = '{type_}' AND osm_id = {id})")

    def exitIdRangeMatch(self, ctx: ParserRuleContext):
        child = ctx.getChild(3).getText()
        lower_bound, upper_bound = child.split("..")
        if lower_bound and upper_bound:
            self.stack.append(f"(osm_id >= {lower_bound} AND osm_id <= {upper_bound})")
        elif lower_bound:
            self.stack.append(f"osm_id >= {lower_bound}")
        elif upper_bound:
            self.stack.append(f"osm_id <= {upper_bound}")

    def exitIdListMatch(self, ctx: ParserRuleContext):
        # differs from TagListMatch insofar that no STRING needs to be popped from stack
        values = []
        children = list(child.getText() for child in ctx.getChildren())
        # skip first part denoting "id:(" as well as last part closing list with ")"
        for child in children[3:-1]:
            # skip comma in list in between brackets
            if child == ",":
                continue
            values.append(child)
        values_as_string = ", ".join(values)
        self.stack.append(f"osm_id IN ({values_as_string})")

    def exitTypeIdListMatch(self, ctx: ParserRuleContext):
        values = []
        children = list(child.getText() for child in ctx.getChildren())
        # skip first part denoting "id:(" as well as last part closing list with ")"
        for child in children[3:-1]:
            # skip comma in list in between brackets
            if child == ",":
                continue
            type_, id = child.split("/")
            values.append(f"(osm_id = {id} AND osm_type = '{type_}')")
        if len(values) > 1:
            values_as_string = "(" + " OR ".join(values) + ")"
        else:
            values_as_string = " OR ".join(values)
        self.stack.append(values_as_string)

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
        child = ctx.getChild(3).getText()
        lower_bound, upper_bound = child.split("..")
        if lower_bound and upper_bound:
            self.stack.append(f"(area >= {lower_bound} AND area <= {upper_bound})")
        elif lower_bound:
            self.stack.append(f"area >= {lower_bound}")
        elif upper_bound:
            self.stack.append(f"area <= {upper_bound}")

    def exitLengthRangeMatch(self, ctx: ParserRuleContext):
        child = ctx.getChild(3).getText()
        lower_bound, upper_bound = child.split("..")
        if lower_bound and upper_bound:
            self.stack.append(f"(length >= {lower_bound} AND length <= {upper_bound})")
        elif lower_bound:
            self.stack.append(f"length >= {lower_bound}")
        elif upper_bound:
            self.stack.append(f"length <= {upper_bound}")

    def exitGeometryVerticesRangeMatch(self, ctx: ParserRuleContext):
        # TODO
        pass

    def exitGeometryOutersMatch(self, ctx: ParserRuleContext):
        # TODO
        pass

    def exitGeometryOutersRangeMatch(self, ctx: ParserRuleContext):
        # TODO
        pass

    def exitGeometryInnersMatch(self, ctx: ParserRuleContext):
        # TODO
        pass

    def exitGeometryInnersRangeMatch(self, ctx: ParserRuleContext):
        # TODO
        pass

    # ---
    #
    def exitChangesetMatch(self, ctx: ParserRuleContext):
        id = ctx.getChild(2).getText()
        self.stack.append(f"changeset_id = {id}")

    def exitChangesetListMatch(self, ctx: ParserRuleContext):
        values = []
        children = list(child.getText() for child in ctx.getChildren())
        # skip first part denoting "id:(" as well as last part closing list with ")"
        for child in children[3:-1]:
            # skip comma in list in between brackets
            if child == ",":
                continue
            values.append(child)
        values_as_string = ", ".join(values)
        self.stack.append(f"changeset_id IN ({values_as_string})")

    def exitChangesetRangeMatch(self, ctx: ParserRuleContext):
        child = ctx.getChild(3).getText()
        lower_bound, upper_bound = child.split("..")
        if lower_bound and upper_bound:
            self.stack.append(
                f"(changeset_id >= {lower_bound} AND changeset_id <= {upper_bound})"
            )
        elif lower_bound:
            self.stack.append(f"changeset_id >= {lower_bound}")
        elif upper_bound:
            self.stack.append(f"changeset_id <= {upper_bound}")

    def exitChangesetCreatedByMatch(self, ctx: ParserRuleContext):
        editor = self.stack.pop()
        j = json.dumps({"created_by": editor})
        self.stack.append(f"changeset_tags @> '{j}'")


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


def ohsome_filter_to_sql(filter: str) -> str:
    listener = OFLToSql()
    tree = build_tree(filter)
    translation = walk_tree(tree, listener).stack
    return " ".join(translation)


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
