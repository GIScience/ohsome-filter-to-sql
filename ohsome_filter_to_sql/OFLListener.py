# Generated from OFL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .OFLParser import OFLParser
else:
    from OFLParser import OFLParser

# This class defines a complete listener for a parse tree produced by OFLParser.
class OFLListener(ParseTreeListener):

    # Enter a parse tree produced by OFLParser#root.
    def enterRoot(self, ctx:OFLParser.RootContext):
        pass

    # Exit a parse tree produced by OFLParser#root.
    def exitRoot(self, ctx:OFLParser.RootContext):
        pass


    # Enter a parse tree produced by OFLParser#expression.
    def enterExpression(self, ctx:OFLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by OFLParser#expression.
    def exitExpression(self, ctx:OFLParser.ExpressionContext):
        pass


    # Enter a parse tree produced by OFLParser#tagMatch.
    def enterTagMatch(self, ctx:OFLParser.TagMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#tagMatch.
    def exitTagMatch(self, ctx:OFLParser.TagMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#tagWildcardMatch.
    def enterTagWildcardMatch(self, ctx:OFLParser.TagWildcardMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#tagWildcardMatch.
    def exitTagWildcardMatch(self, ctx:OFLParser.TagWildcardMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#tagListMatch.
    def enterTagListMatch(self, ctx:OFLParser.TagListMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#tagListMatch.
    def exitTagListMatch(self, ctx:OFLParser.TagListMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#tagNotMatch.
    def enterTagNotMatch(self, ctx:OFLParser.TagNotMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#tagNotMatch.
    def exitTagNotMatch(self, ctx:OFLParser.TagNotMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#tagNotWildcardMatch.
    def enterTagNotWildcardMatch(self, ctx:OFLParser.TagNotWildcardMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#tagNotWildcardMatch.
    def exitTagNotWildcardMatch(self, ctx:OFLParser.TagNotWildcardMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#hashtagMatch.
    def enterHashtagMatch(self, ctx:OFLParser.HashtagMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#hashtagMatch.
    def exitHashtagMatch(self, ctx:OFLParser.HashtagMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#hashtagWildcardMatch.
    def enterHashtagWildcardMatch(self, ctx:OFLParser.HashtagWildcardMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#hashtagWildcardMatch.
    def exitHashtagWildcardMatch(self, ctx:OFLParser.HashtagWildcardMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#hashtagListMatch.
    def enterHashtagListMatch(self, ctx:OFLParser.HashtagListMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#hashtagListMatch.
    def exitHashtagListMatch(self, ctx:OFLParser.HashtagListMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#typeMatch.
    def enterTypeMatch(self, ctx:OFLParser.TypeMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#typeMatch.
    def exitTypeMatch(self, ctx:OFLParser.TypeMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#idMatch.
    def enterIdMatch(self, ctx:OFLParser.IdMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#idMatch.
    def exitIdMatch(self, ctx:OFLParser.IdMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#typeIdMatch.
    def enterTypeIdMatch(self, ctx:OFLParser.TypeIdMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#typeIdMatch.
    def exitTypeIdMatch(self, ctx:OFLParser.TypeIdMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#idRangeMatch.
    def enterIdRangeMatch(self, ctx:OFLParser.IdRangeMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#idRangeMatch.
    def exitIdRangeMatch(self, ctx:OFLParser.IdRangeMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#idListMatch.
    def enterIdListMatch(self, ctx:OFLParser.IdListMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#idListMatch.
    def exitIdListMatch(self, ctx:OFLParser.IdListMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#typeIdListMatch.
    def enterTypeIdListMatch(self, ctx:OFLParser.TypeIdListMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#typeIdListMatch.
    def exitTypeIdListMatch(self, ctx:OFLParser.TypeIdListMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#geometryMatch.
    def enterGeometryMatch(self, ctx:OFLParser.GeometryMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#geometryMatch.
    def exitGeometryMatch(self, ctx:OFLParser.GeometryMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#areaRangeMatch.
    def enterAreaRangeMatch(self, ctx:OFLParser.AreaRangeMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#areaRangeMatch.
    def exitAreaRangeMatch(self, ctx:OFLParser.AreaRangeMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#perimeterRangeMatch.
    def enterPerimeterRangeMatch(self, ctx:OFLParser.PerimeterRangeMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#perimeterRangeMatch.
    def exitPerimeterRangeMatch(self, ctx:OFLParser.PerimeterRangeMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#lengthRangeMatch.
    def enterLengthRangeMatch(self, ctx:OFLParser.LengthRangeMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#lengthRangeMatch.
    def exitLengthRangeMatch(self, ctx:OFLParser.LengthRangeMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#geometryVerticesRangeMatch.
    def enterGeometryVerticesRangeMatch(self, ctx:OFLParser.GeometryVerticesRangeMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#geometryVerticesRangeMatch.
    def exitGeometryVerticesRangeMatch(self, ctx:OFLParser.GeometryVerticesRangeMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#geometryOutersMatch.
    def enterGeometryOutersMatch(self, ctx:OFLParser.GeometryOutersMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#geometryOutersMatch.
    def exitGeometryOutersMatch(self, ctx:OFLParser.GeometryOutersMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#geometryOutersRangeMatch.
    def enterGeometryOutersRangeMatch(self, ctx:OFLParser.GeometryOutersRangeMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#geometryOutersRangeMatch.
    def exitGeometryOutersRangeMatch(self, ctx:OFLParser.GeometryOutersRangeMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#geometryInnersMatch.
    def enterGeometryInnersMatch(self, ctx:OFLParser.GeometryInnersMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#geometryInnersMatch.
    def exitGeometryInnersMatch(self, ctx:OFLParser.GeometryInnersMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#geometryInnersRangeMatch.
    def enterGeometryInnersRangeMatch(self, ctx:OFLParser.GeometryInnersRangeMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#geometryInnersRangeMatch.
    def exitGeometryInnersRangeMatch(self, ctx:OFLParser.GeometryInnersRangeMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#changesetMatch.
    def enterChangesetMatch(self, ctx:OFLParser.ChangesetMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#changesetMatch.
    def exitChangesetMatch(self, ctx:OFLParser.ChangesetMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#changesetListMatch.
    def enterChangesetListMatch(self, ctx:OFLParser.ChangesetListMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#changesetListMatch.
    def exitChangesetListMatch(self, ctx:OFLParser.ChangesetListMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#changesetRangeMatch.
    def enterChangesetRangeMatch(self, ctx:OFLParser.ChangesetRangeMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#changesetRangeMatch.
    def exitChangesetRangeMatch(self, ctx:OFLParser.ChangesetRangeMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#changesetCreatedByMatch.
    def enterChangesetCreatedByMatch(self, ctx:OFLParser.ChangesetCreatedByMatchContext):
        pass

    # Exit a parse tree produced by OFLParser#changesetCreatedByMatch.
    def exitChangesetCreatedByMatch(self, ctx:OFLParser.ChangesetCreatedByMatchContext):
        pass


    # Enter a parse tree produced by OFLParser#string.
    def enterString(self, ctx:OFLParser.StringContext):
        pass

    # Exit a parse tree produced by OFLParser#string.
    def exitString(self, ctx:OFLParser.StringContext):
        pass



del OFLParser