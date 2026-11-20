# Generated from OFLC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .OFLCParser import OFLCParser
else:
    from OFLCParser import OFLCParser

# This class defines a complete listener for a parse tree produced by OFLCParser.
class OFLCListener(ParseTreeListener):

    # Enter a parse tree produced by OFLCParser#root.
    def enterRoot(self, ctx:OFLCParser.RootContext):
        pass

    # Exit a parse tree produced by OFLCParser#root.
    def exitRoot(self, ctx:OFLCParser.RootContext):
        pass


    # Enter a parse tree produced by OFLCParser#expression.
    def enterExpression(self, ctx:OFLCParser.ExpressionContext):
        pass

    # Exit a parse tree produced by OFLCParser#expression.
    def exitExpression(self, ctx:OFLCParser.ExpressionContext):
        pass


    # Enter a parse tree produced by OFLCParser#tagMatch.
    def enterTagMatch(self, ctx:OFLCParser.TagMatchContext):
        pass

    # Exit a parse tree produced by OFLCParser#tagMatch.
    def exitTagMatch(self, ctx:OFLCParser.TagMatchContext):
        pass


    # Enter a parse tree produced by OFLCParser#tagWildcardMatch.
    def enterTagWildcardMatch(self, ctx:OFLCParser.TagWildcardMatchContext):
        pass

    # Exit a parse tree produced by OFLCParser#tagWildcardMatch.
    def exitTagWildcardMatch(self, ctx:OFLCParser.TagWildcardMatchContext):
        pass


    # Enter a parse tree produced by OFLCParser#tagListMatch.
    def enterTagListMatch(self, ctx:OFLCParser.TagListMatchContext):
        pass

    # Exit a parse tree produced by OFLCParser#tagListMatch.
    def exitTagListMatch(self, ctx:OFLCParser.TagListMatchContext):
        pass


    # Enter a parse tree produced by OFLCParser#tagNotMatch.
    def enterTagNotMatch(self, ctx:OFLCParser.TagNotMatchContext):
        pass

    # Exit a parse tree produced by OFLCParser#tagNotMatch.
    def exitTagNotMatch(self, ctx:OFLCParser.TagNotMatchContext):
        pass


    # Enter a parse tree produced by OFLCParser#tagNotWildcardMatch.
    def enterTagNotWildcardMatch(self, ctx:OFLCParser.TagNotWildcardMatchContext):
        pass

    # Exit a parse tree produced by OFLCParser#tagNotWildcardMatch.
    def exitTagNotWildcardMatch(self, ctx:OFLCParser.TagNotWildcardMatchContext):
        pass


    # Enter a parse tree produced by OFLCParser#tagValuePatternMatch.
    def enterTagValuePatternMatch(self, ctx:OFLCParser.TagValuePatternMatchContext):
        pass

    # Exit a parse tree produced by OFLCParser#tagValuePatternMatch.
    def exitTagValuePatternMatch(self, ctx:OFLCParser.TagValuePatternMatchContext):
        pass


    # Enter a parse tree produced by OFLCParser#idMatch.
    def enterIdMatch(self, ctx:OFLCParser.IdMatchContext):
        pass

    # Exit a parse tree produced by OFLCParser#idMatch.
    def exitIdMatch(self, ctx:OFLCParser.IdMatchContext):
        pass


    # Enter a parse tree produced by OFLCParser#idRangeMatch.
    def enterIdRangeMatch(self, ctx:OFLCParser.IdRangeMatchContext):
        pass

    # Exit a parse tree produced by OFLCParser#idRangeMatch.
    def exitIdRangeMatch(self, ctx:OFLCParser.IdRangeMatchContext):
        pass


    # Enter a parse tree produced by OFLCParser#idListMatch.
    def enterIdListMatch(self, ctx:OFLCParser.IdListMatchContext):
        pass

    # Exit a parse tree produced by OFLCParser#idListMatch.
    def exitIdListMatch(self, ctx:OFLCParser.IdListMatchContext):
        pass


    # Enter a parse tree produced by OFLCParser#hashtagMatch.
    def enterHashtagMatch(self, ctx:OFLCParser.HashtagMatchContext):
        pass

    # Exit a parse tree produced by OFLCParser#hashtagMatch.
    def exitHashtagMatch(self, ctx:OFLCParser.HashtagMatchContext):
        pass


    # Enter a parse tree produced by OFLCParser#string.
    def enterString(self, ctx:OFLCParser.StringContext):
        pass

    # Exit a parse tree produced by OFLCParser#string.
    def exitString(self, ctx:OFLCParser.StringContext):
        pass


    # Enter a parse tree produced by OFLCParser#valueSubString.
    def enterValueSubString(self, ctx:OFLCParser.ValueSubStringContext):
        pass

    # Exit a parse tree produced by OFLCParser#valueSubString.
    def exitValueSubString(self, ctx:OFLCParser.ValueSubStringContext):
        pass


    # Enter a parse tree produced by OFLCParser#hashtagString.
    def enterHashtagString(self, ctx:OFLCParser.HashtagStringContext):
        pass

    # Exit a parse tree produced by OFLCParser#hashtagString.
    def exitHashtagString(self, ctx:OFLCParser.HashtagStringContext):
        pass


    # Enter a parse tree produced by OFLCParser#and.
    def enterAnd(self, ctx:OFLCParser.AndContext):
        pass

    # Exit a parse tree produced by OFLCParser#and.
    def exitAnd(self, ctx:OFLCParser.AndContext):
        pass


    # Enter a parse tree produced by OFLCParser#or.
    def enterOr(self, ctx:OFLCParser.OrContext):
        pass

    # Exit a parse tree produced by OFLCParser#or.
    def exitOr(self, ctx:OFLCParser.OrContext):
        pass


    # Enter a parse tree produced by OFLCParser#not.
    def enterNot(self, ctx:OFLCParser.NotContext):
        pass

    # Exit a parse tree produced by OFLCParser#not.
    def exitNot(self, ctx:OFLCParser.NotContext):
        pass


    # Enter a parse tree produced by OFLCParser#in.
    def enterIn(self, ctx:OFLCParser.InContext):
        pass

    # Exit a parse tree produced by OFLCParser#in.
    def exitIn(self, ctx:OFLCParser.InContext):
        pass


    # Enter a parse tree produced by OFLCParser#eq.
    def enterEq(self, ctx:OFLCParser.EqContext):
        pass

    # Exit a parse tree produced by OFLCParser#eq.
    def exitEq(self, ctx:OFLCParser.EqContext):
        pass


    # Enter a parse tree produced by OFLCParser#ne.
    def enterNe(self, ctx:OFLCParser.NeContext):
        pass

    # Exit a parse tree produced by OFLCParser#ne.
    def exitNe(self, ctx:OFLCParser.NeContext):
        pass


    # Enter a parse tree produced by OFLCParser#po.
    def enterPo(self, ctx:OFLCParser.PoContext):
        pass

    # Exit a parse tree produced by OFLCParser#po.
    def exitPo(self, ctx:OFLCParser.PoContext):
        pass


    # Enter a parse tree produced by OFLCParser#pc.
    def enterPc(self, ctx:OFLCParser.PcContext):
        pass

    # Exit a parse tree produced by OFLCParser#pc.
    def exitPc(self, ctx:OFLCParser.PcContext):
        pass


    # Enter a parse tree produced by OFLCParser#co.
    def enterCo(self, ctx:OFLCParser.CoContext):
        pass

    # Exit a parse tree produced by OFLCParser#co.
    def exitCo(self, ctx:OFLCParser.CoContext):
        pass


    # Enter a parse tree produced by OFLCParser#dd.
    def enterDd(self, ctx:OFLCParser.DdContext):
        pass

    # Exit a parse tree produced by OFLCParser#dd.
    def exitDd(self, ctx:OFLCParser.DdContext):
        pass


    # Enter a parse tree produced by OFLCParser#cn.
    def enterCn(self, ctx:OFLCParser.CnContext):
        pass

    # Exit a parse tree produced by OFLCParser#cn.
    def exitCn(self, ctx:OFLCParser.CnContext):
        pass


    # Enter a parse tree produced by OFLCParser#tl.
    def enterTl(self, ctx:OFLCParser.TlContext):
        pass

    # Exit a parse tree produced by OFLCParser#tl.
    def exitTl(self, ctx:OFLCParser.TlContext):
        pass


    # Enter a parse tree produced by OFLCParser#range_int.
    def enterRange_int(self, ctx:OFLCParser.Range_intContext):
        pass

    # Exit a parse tree produced by OFLCParser#range_int.
    def exitRange_int(self, ctx:OFLCParser.Range_intContext):
        pass



del OFLCParser