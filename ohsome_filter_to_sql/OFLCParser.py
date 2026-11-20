# Generated from OFLC.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,286,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,3,0,58,8,0,1,0,1,0,3,0,62,8,0,1,0,3,0,65,8,0,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,3,1,87,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,97,8,1,
        10,1,12,1,100,9,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,5,4,117,8,4,10,4,12,4,120,9,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,
        1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,151,8,10,10,10,12,10,
        154,9,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,
        3,12,167,8,12,5,12,169,8,12,10,12,12,12,172,9,12,3,12,174,8,12,1,
        13,3,13,177,8,13,1,13,1,13,3,13,181,8,13,1,14,1,14,1,14,3,14,186,
        8,14,1,15,3,15,189,8,15,1,15,1,15,3,15,193,8,15,1,16,3,16,196,8,
        16,1,16,1,16,3,16,200,8,16,1,17,3,17,203,8,17,1,17,1,17,3,17,207,
        8,17,1,18,3,18,210,8,18,1,18,1,18,3,18,214,8,18,1,19,3,19,217,8,
        19,1,19,1,19,3,19,221,8,19,1,20,3,20,224,8,20,1,20,1,20,3,20,228,
        8,20,1,21,3,21,231,8,21,1,21,1,21,3,21,235,8,21,1,22,3,22,238,8,
        22,1,22,1,22,3,22,242,8,22,1,23,3,23,245,8,23,1,23,1,23,3,23,249,
        8,23,1,24,3,24,252,8,24,1,24,1,24,3,24,256,8,24,1,25,3,25,259,8,
        25,1,25,1,25,3,25,263,8,25,1,26,3,26,266,8,26,1,26,1,26,3,26,270,
        8,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,282,
        8,27,1,27,1,27,1,27,0,1,2,28,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,54,0,1,3,0,10,13,15,16,19,
        19,308,0,57,1,0,0,0,2,86,1,0,0,0,4,101,1,0,0,0,6,105,1,0,0,0,8,109,
        1,0,0,0,10,123,1,0,0,0,12,127,1,0,0,0,14,131,1,0,0,0,16,135,1,0,
        0,0,18,139,1,0,0,0,20,143,1,0,0,0,22,157,1,0,0,0,24,173,1,0,0,0,
        26,176,1,0,0,0,28,185,1,0,0,0,30,188,1,0,0,0,32,195,1,0,0,0,34,202,
        1,0,0,0,36,209,1,0,0,0,38,216,1,0,0,0,40,223,1,0,0,0,42,230,1,0,
        0,0,44,237,1,0,0,0,46,244,1,0,0,0,48,251,1,0,0,0,50,258,1,0,0,0,
        52,265,1,0,0,0,54,271,1,0,0,0,56,58,5,21,0,0,57,56,1,0,0,0,57,58,
        1,0,0,0,58,61,1,0,0,0,59,62,3,2,1,0,60,62,5,14,0,0,61,59,1,0,0,0,
        61,60,1,0,0,0,62,64,1,0,0,0,63,65,5,21,0,0,64,63,1,0,0,0,64,65,1,
        0,0,0,65,66,1,0,0,0,66,67,5,0,0,1,67,1,1,0,0,0,68,69,6,1,-1,0,69,
        70,3,42,21,0,70,71,3,2,1,0,71,72,3,44,22,0,72,87,1,0,0,0,73,74,3,
        34,17,0,74,75,3,2,1,13,75,87,1,0,0,0,76,87,3,4,2,0,77,87,3,6,3,0,
        78,87,3,10,5,0,79,87,3,12,6,0,80,87,3,8,4,0,81,87,3,14,7,0,82,87,
        3,16,8,0,83,87,3,18,9,0,84,87,3,20,10,0,85,87,3,22,11,0,86,68,1,
        0,0,0,86,73,1,0,0,0,86,76,1,0,0,0,86,77,1,0,0,0,86,78,1,0,0,0,86,
        79,1,0,0,0,86,80,1,0,0,0,86,81,1,0,0,0,86,82,1,0,0,0,86,83,1,0,0,
        0,86,84,1,0,0,0,86,85,1,0,0,0,87,98,1,0,0,0,88,89,10,12,0,0,89,90,
        3,30,15,0,90,91,3,2,1,13,91,97,1,0,0,0,92,93,10,11,0,0,93,94,3,32,
        16,0,94,95,3,2,1,12,95,97,1,0,0,0,96,88,1,0,0,0,96,92,1,0,0,0,97,
        100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,3,1,0,0,0,100,98,1,0,
        0,0,101,102,3,24,12,0,102,103,3,38,19,0,103,104,3,24,12,0,104,5,
        1,0,0,0,105,106,3,24,12,0,106,107,3,38,19,0,107,108,5,14,0,0,108,
        7,1,0,0,0,109,110,3,24,12,0,110,111,3,36,18,0,111,112,3,42,21,0,
        112,118,3,24,12,0,113,114,3,46,23,0,114,115,3,24,12,0,115,117,1,
        0,0,0,116,113,1,0,0,0,117,120,1,0,0,0,118,116,1,0,0,0,118,119,1,
        0,0,0,119,121,1,0,0,0,120,118,1,0,0,0,121,122,3,44,22,0,122,9,1,
        0,0,0,123,124,3,24,12,0,124,125,3,40,20,0,125,126,3,24,12,0,126,
        11,1,0,0,0,127,128,3,24,12,0,128,129,3,40,20,0,129,130,5,14,0,0,
        130,13,1,0,0,0,131,132,3,24,12,0,132,133,3,52,26,0,133,134,3,26,
        13,0,134,15,1,0,0,0,135,136,5,15,0,0,136,137,3,50,25,0,137,138,5,
        17,0,0,138,17,1,0,0,0,139,140,5,15,0,0,140,141,3,50,25,0,141,142,
        3,54,27,0,142,19,1,0,0,0,143,144,5,15,0,0,144,145,3,50,25,0,145,
        146,3,42,21,0,146,152,5,17,0,0,147,148,3,46,23,0,148,149,5,17,0,
        0,149,151,1,0,0,0,150,147,1,0,0,0,151,154,1,0,0,0,152,150,1,0,0,
        0,152,153,1,0,0,0,153,155,1,0,0,0,154,152,1,0,0,0,155,156,3,44,22,
        0,156,21,1,0,0,0,157,158,5,16,0,0,158,159,3,50,25,0,159,160,3,28,
        14,0,160,23,1,0,0,0,161,174,5,20,0,0,162,174,5,17,0,0,163,170,7,
        0,0,0,164,166,5,1,0,0,165,167,7,0,0,0,166,165,1,0,0,0,166,167,1,
        0,0,0,167,169,1,0,0,0,168,164,1,0,0,0,169,172,1,0,0,0,170,168,1,
        0,0,0,170,171,1,0,0,0,171,174,1,0,0,0,172,170,1,0,0,0,173,161,1,
        0,0,0,173,162,1,0,0,0,173,163,1,0,0,0,174,25,1,0,0,0,175,177,5,14,
        0,0,176,175,1,0,0,0,176,177,1,0,0,0,177,178,1,0,0,0,178,180,3,24,
        12,0,179,181,5,14,0,0,180,179,1,0,0,0,180,181,1,0,0,0,181,27,1,0,
        0,0,182,183,5,2,0,0,183,186,5,19,0,0,184,186,3,24,12,0,185,182,1,
        0,0,0,185,184,1,0,0,0,186,29,1,0,0,0,187,189,5,21,0,0,188,187,1,
        0,0,0,188,189,1,0,0,0,189,190,1,0,0,0,190,192,5,10,0,0,191,193,5,
        21,0,0,192,191,1,0,0,0,192,193,1,0,0,0,193,31,1,0,0,0,194,196,5,
        21,0,0,195,194,1,0,0,0,195,196,1,0,0,0,196,197,1,0,0,0,197,199,5,
        11,0,0,198,200,5,21,0,0,199,198,1,0,0,0,199,200,1,0,0,0,200,33,1,
        0,0,0,201,203,5,21,0,0,202,201,1,0,0,0,202,203,1,0,0,0,203,204,1,
        0,0,0,204,206,5,12,0,0,205,207,5,21,0,0,206,205,1,0,0,0,206,207,
        1,0,0,0,207,35,1,0,0,0,208,210,5,21,0,0,209,208,1,0,0,0,209,210,
        1,0,0,0,210,211,1,0,0,0,211,213,5,13,0,0,212,214,5,21,0,0,213,212,
        1,0,0,0,213,214,1,0,0,0,214,37,1,0,0,0,215,217,5,21,0,0,216,215,
        1,0,0,0,216,217,1,0,0,0,217,218,1,0,0,0,218,220,5,3,0,0,219,221,
        5,21,0,0,220,219,1,0,0,0,220,221,1,0,0,0,221,39,1,0,0,0,222,224,
        5,21,0,0,223,222,1,0,0,0,223,224,1,0,0,0,224,225,1,0,0,0,225,227,
        5,4,0,0,226,228,5,21,0,0,227,226,1,0,0,0,227,228,1,0,0,0,228,41,
        1,0,0,0,229,231,5,21,0,0,230,229,1,0,0,0,230,231,1,0,0,0,231,232,
        1,0,0,0,232,234,5,5,0,0,233,235,5,21,0,0,234,233,1,0,0,0,234,235,
        1,0,0,0,235,43,1,0,0,0,236,238,5,21,0,0,237,236,1,0,0,0,237,238,
        1,0,0,0,238,239,1,0,0,0,239,241,5,6,0,0,240,242,5,21,0,0,241,240,
        1,0,0,0,241,242,1,0,0,0,242,45,1,0,0,0,243,245,5,21,0,0,244,243,
        1,0,0,0,244,245,1,0,0,0,245,246,1,0,0,0,246,248,5,7,0,0,247,249,
        5,21,0,0,248,247,1,0,0,0,248,249,1,0,0,0,249,47,1,0,0,0,250,252,
        5,21,0,0,251,250,1,0,0,0,251,252,1,0,0,0,252,253,1,0,0,0,253,255,
        5,8,0,0,254,256,5,21,0,0,255,254,1,0,0,0,255,256,1,0,0,0,256,49,
        1,0,0,0,257,259,5,21,0,0,258,257,1,0,0,0,258,259,1,0,0,0,259,260,
        1,0,0,0,260,262,5,1,0,0,261,263,5,21,0,0,262,261,1,0,0,0,262,263,
        1,0,0,0,263,51,1,0,0,0,264,266,5,21,0,0,265,264,1,0,0,0,265,266,
        1,0,0,0,266,267,1,0,0,0,267,269,5,9,0,0,268,270,5,21,0,0,269,268,
        1,0,0,0,269,270,1,0,0,0,270,53,1,0,0,0,271,281,3,42,21,0,272,273,
        5,17,0,0,273,274,3,48,24,0,274,275,5,17,0,0,275,282,1,0,0,0,276,
        277,3,48,24,0,277,278,5,17,0,0,278,282,1,0,0,0,279,280,5,17,0,0,
        280,282,3,48,24,0,281,272,1,0,0,0,281,276,1,0,0,0,281,279,1,0,0,
        0,282,283,1,0,0,0,283,284,3,44,22,0,284,55,1,0,0,0,39,57,61,64,86,
        96,98,118,152,166,170,173,176,180,185,188,192,195,199,202,206,209,
        213,216,220,223,227,230,234,237,241,244,248,251,255,258,262,265,
        269,281
    ]

class OFLCParser ( Parser ):

    grammarFileName = "OFLC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'#'", "'='", "'!='", "'('", "')'", 
                     "','", "'..'", "'~'", "'and'", "'or'", "'not'", "'in'", 
                     "'*'", "'id'", "'hashtag'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "AND", "OR", "NOT", "IN", 
                      "WILDCARD", "ID", "HASHTAG", "NUMBER", "DECIMAL", 
                      "WORD", "QUOTED", "WS" ]

    RULE_root = 0
    RULE_expression = 1
    RULE_tagMatch = 2
    RULE_tagWildcardMatch = 3
    RULE_tagListMatch = 4
    RULE_tagNotMatch = 5
    RULE_tagNotWildcardMatch = 6
    RULE_tagValuePatternMatch = 7
    RULE_idMatch = 8
    RULE_idRangeMatch = 9
    RULE_idListMatch = 10
    RULE_hashtagMatch = 11
    RULE_string = 12
    RULE_valueSubString = 13
    RULE_hashtagString = 14
    RULE_and = 15
    RULE_or = 16
    RULE_not = 17
    RULE_in = 18
    RULE_eq = 19
    RULE_ne = 20
    RULE_po = 21
    RULE_pc = 22
    RULE_co = 23
    RULE_dd = 24
    RULE_cn = 25
    RULE_tl = 26
    RULE_range_int = 27

    ruleNames =  [ "root", "expression", "tagMatch", "tagWildcardMatch", 
                   "tagListMatch", "tagNotMatch", "tagNotWildcardMatch", 
                   "tagValuePatternMatch", "idMatch", "idRangeMatch", "idListMatch", 
                   "hashtagMatch", "string", "valueSubString", "hashtagString", 
                   "and", "or", "not", "in", "eq", "ne", "po", "pc", "co", 
                   "dd", "cn", "tl", "range_int" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    AND=10
    OR=11
    NOT=12
    IN=13
    WILDCARD=14
    ID=15
    HASHTAG=16
    NUMBER=17
    DECIMAL=18
    WORD=19
    QUOTED=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(OFLCParser.EOF, 0)

        def expression(self):
            return self.getTypedRuleContext(OFLCParser.ExpressionContext,0)


        def WILDCARD(self):
            return self.getToken(OFLCParser.WILDCARD, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(OFLCParser.WS)
            else:
                return self.getToken(OFLCParser.WS, i)

        def getRuleIndex(self):
            return OFLCParser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)




    def root(self):

        localctx = OFLCParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 56
                self.match(OFLCParser.WS)


            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 10, 11, 12, 13, 15, 16, 17, 19, 20, 21]:
                self.state = 59
                self.expression(0)
                pass
            elif token in [14]:
                self.state = 60
                self.match(OFLCParser.WILDCARD)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 63
                self.match(OFLCParser.WS)


            self.state = 66
            self.match(OFLCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def po(self):
            return self.getTypedRuleContext(OFLCParser.PoContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OFLCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OFLCParser.ExpressionContext,i)


        def pc(self):
            return self.getTypedRuleContext(OFLCParser.PcContext,0)


        def not_(self):
            return self.getTypedRuleContext(OFLCParser.NotContext,0)


        def tagMatch(self):
            return self.getTypedRuleContext(OFLCParser.TagMatchContext,0)


        def tagWildcardMatch(self):
            return self.getTypedRuleContext(OFLCParser.TagWildcardMatchContext,0)


        def tagNotMatch(self):
            return self.getTypedRuleContext(OFLCParser.TagNotMatchContext,0)


        def tagNotWildcardMatch(self):
            return self.getTypedRuleContext(OFLCParser.TagNotWildcardMatchContext,0)


        def tagListMatch(self):
            return self.getTypedRuleContext(OFLCParser.TagListMatchContext,0)


        def tagValuePatternMatch(self):
            return self.getTypedRuleContext(OFLCParser.TagValuePatternMatchContext,0)


        def idMatch(self):
            return self.getTypedRuleContext(OFLCParser.IdMatchContext,0)


        def idRangeMatch(self):
            return self.getTypedRuleContext(OFLCParser.IdRangeMatchContext,0)


        def idListMatch(self):
            return self.getTypedRuleContext(OFLCParser.IdListMatchContext,0)


        def hashtagMatch(self):
            return self.getTypedRuleContext(OFLCParser.HashtagMatchContext,0)


        def and_(self):
            return self.getTypedRuleContext(OFLCParser.AndContext,0)


        def or_(self):
            return self.getTypedRuleContext(OFLCParser.OrContext,0)


        def getRuleIndex(self):
            return OFLCParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OFLCParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 69
                self.po()
                self.state = 70
                self.expression(0)
                self.state = 71
                self.pc()
                pass

            elif la_ == 2:
                self.state = 73
                self.not_()
                self.state = 74
                self.expression(13)
                pass

            elif la_ == 3:
                self.state = 76
                self.tagMatch()
                pass

            elif la_ == 4:
                self.state = 77
                self.tagWildcardMatch()
                pass

            elif la_ == 5:
                self.state = 78
                self.tagNotMatch()
                pass

            elif la_ == 6:
                self.state = 79
                self.tagNotWildcardMatch()
                pass

            elif la_ == 7:
                self.state = 80
                self.tagListMatch()
                pass

            elif la_ == 8:
                self.state = 81
                self.tagValuePatternMatch()
                pass

            elif la_ == 9:
                self.state = 82
                self.idMatch()
                pass

            elif la_ == 10:
                self.state = 83
                self.idRangeMatch()
                pass

            elif la_ == 11:
                self.state = 84
                self.idListMatch()
                pass

            elif la_ == 12:
                self.state = 85
                self.hashtagMatch()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 98
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 96
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = OFLCParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 88
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 89
                        self.and_()
                        self.state = 90
                        self.expression(13)
                        pass

                    elif la_ == 2:
                        localctx = OFLCParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 92
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 93
                        self.or_()
                        self.state = 94
                        self.expression(12)
                        pass

             
                self.state = 100
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TagMatchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OFLCParser.StringContext)
            else:
                return self.getTypedRuleContext(OFLCParser.StringContext,i)


        def eq(self):
            return self.getTypedRuleContext(OFLCParser.EqContext,0)


        def getRuleIndex(self):
            return OFLCParser.RULE_tagMatch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTagMatch" ):
                listener.enterTagMatch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTagMatch" ):
                listener.exitTagMatch(self)




    def tagMatch(self):

        localctx = OFLCParser.TagMatchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_tagMatch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.string()
            self.state = 102
            self.eq()
            self.state = 103
            self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TagWildcardMatchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(OFLCParser.StringContext,0)


        def eq(self):
            return self.getTypedRuleContext(OFLCParser.EqContext,0)


        def WILDCARD(self):
            return self.getToken(OFLCParser.WILDCARD, 0)

        def getRuleIndex(self):
            return OFLCParser.RULE_tagWildcardMatch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTagWildcardMatch" ):
                listener.enterTagWildcardMatch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTagWildcardMatch" ):
                listener.exitTagWildcardMatch(self)




    def tagWildcardMatch(self):

        localctx = OFLCParser.TagWildcardMatchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tagWildcardMatch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.string()
            self.state = 106
            self.eq()
            self.state = 107
            self.match(OFLCParser.WILDCARD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TagListMatchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OFLCParser.StringContext)
            else:
                return self.getTypedRuleContext(OFLCParser.StringContext,i)


        def in_(self):
            return self.getTypedRuleContext(OFLCParser.InContext,0)


        def po(self):
            return self.getTypedRuleContext(OFLCParser.PoContext,0)


        def pc(self):
            return self.getTypedRuleContext(OFLCParser.PcContext,0)


        def co(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OFLCParser.CoContext)
            else:
                return self.getTypedRuleContext(OFLCParser.CoContext,i)


        def getRuleIndex(self):
            return OFLCParser.RULE_tagListMatch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTagListMatch" ):
                listener.enterTagListMatch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTagListMatch" ):
                listener.exitTagListMatch(self)




    def tagListMatch(self):

        localctx = OFLCParser.TagListMatchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tagListMatch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.string()
            self.state = 110
            self.in_()
            self.state = 111
            self.po()
            self.state = 112
            self.string()
            self.state = 118
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 113
                    self.co()
                    self.state = 114
                    self.string() 
                self.state = 120
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 121
            self.pc()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TagNotMatchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OFLCParser.StringContext)
            else:
                return self.getTypedRuleContext(OFLCParser.StringContext,i)


        def ne(self):
            return self.getTypedRuleContext(OFLCParser.NeContext,0)


        def getRuleIndex(self):
            return OFLCParser.RULE_tagNotMatch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTagNotMatch" ):
                listener.enterTagNotMatch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTagNotMatch" ):
                listener.exitTagNotMatch(self)




    def tagNotMatch(self):

        localctx = OFLCParser.TagNotMatchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tagNotMatch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.string()
            self.state = 124
            self.ne()
            self.state = 125
            self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TagNotWildcardMatchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(OFLCParser.StringContext,0)


        def ne(self):
            return self.getTypedRuleContext(OFLCParser.NeContext,0)


        def WILDCARD(self):
            return self.getToken(OFLCParser.WILDCARD, 0)

        def getRuleIndex(self):
            return OFLCParser.RULE_tagNotWildcardMatch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTagNotWildcardMatch" ):
                listener.enterTagNotWildcardMatch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTagNotWildcardMatch" ):
                listener.exitTagNotWildcardMatch(self)




    def tagNotWildcardMatch(self):

        localctx = OFLCParser.TagNotWildcardMatchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tagNotWildcardMatch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.string()
            self.state = 128
            self.ne()
            self.state = 129
            self.match(OFLCParser.WILDCARD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TagValuePatternMatchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(OFLCParser.StringContext,0)


        def tl(self):
            return self.getTypedRuleContext(OFLCParser.TlContext,0)


        def valueSubString(self):
            return self.getTypedRuleContext(OFLCParser.ValueSubStringContext,0)


        def getRuleIndex(self):
            return OFLCParser.RULE_tagValuePatternMatch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTagValuePatternMatch" ):
                listener.enterTagValuePatternMatch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTagValuePatternMatch" ):
                listener.exitTagValuePatternMatch(self)




    def tagValuePatternMatch(self):

        localctx = OFLCParser.TagValuePatternMatchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_tagValuePatternMatch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.string()
            self.state = 132
            self.tl()
            self.state = 133
            self.valueSubString()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdMatchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(OFLCParser.ID, 0)

        def cn(self):
            return self.getTypedRuleContext(OFLCParser.CnContext,0)


        def NUMBER(self):
            return self.getToken(OFLCParser.NUMBER, 0)

        def getRuleIndex(self):
            return OFLCParser.RULE_idMatch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdMatch" ):
                listener.enterIdMatch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdMatch" ):
                listener.exitIdMatch(self)




    def idMatch(self):

        localctx = OFLCParser.IdMatchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_idMatch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(OFLCParser.ID)
            self.state = 136
            self.cn()
            self.state = 137
            self.match(OFLCParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdRangeMatchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(OFLCParser.ID, 0)

        def cn(self):
            return self.getTypedRuleContext(OFLCParser.CnContext,0)


        def range_int(self):
            return self.getTypedRuleContext(OFLCParser.Range_intContext,0)


        def getRuleIndex(self):
            return OFLCParser.RULE_idRangeMatch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdRangeMatch" ):
                listener.enterIdRangeMatch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdRangeMatch" ):
                listener.exitIdRangeMatch(self)




    def idRangeMatch(self):

        localctx = OFLCParser.IdRangeMatchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_idRangeMatch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(OFLCParser.ID)
            self.state = 140
            self.cn()
            self.state = 141
            self.range_int()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdListMatchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(OFLCParser.ID, 0)

        def cn(self):
            return self.getTypedRuleContext(OFLCParser.CnContext,0)


        def po(self):
            return self.getTypedRuleContext(OFLCParser.PoContext,0)


        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(OFLCParser.NUMBER)
            else:
                return self.getToken(OFLCParser.NUMBER, i)

        def pc(self):
            return self.getTypedRuleContext(OFLCParser.PcContext,0)


        def co(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OFLCParser.CoContext)
            else:
                return self.getTypedRuleContext(OFLCParser.CoContext,i)


        def getRuleIndex(self):
            return OFLCParser.RULE_idListMatch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdListMatch" ):
                listener.enterIdListMatch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdListMatch" ):
                listener.exitIdListMatch(self)




    def idListMatch(self):

        localctx = OFLCParser.IdListMatchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_idListMatch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(OFLCParser.ID)
            self.state = 144
            self.cn()
            self.state = 145
            self.po()
            self.state = 146
            self.match(OFLCParser.NUMBER)
            self.state = 152
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 147
                    self.co()
                    self.state = 148
                    self.match(OFLCParser.NUMBER) 
                self.state = 154
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 155
            self.pc()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HashtagMatchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HASHTAG(self):
            return self.getToken(OFLCParser.HASHTAG, 0)

        def cn(self):
            return self.getTypedRuleContext(OFLCParser.CnContext,0)


        def hashtagString(self):
            return self.getTypedRuleContext(OFLCParser.HashtagStringContext,0)


        def getRuleIndex(self):
            return OFLCParser.RULE_hashtagMatch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHashtagMatch" ):
                listener.enterHashtagMatch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHashtagMatch" ):
                listener.exitHashtagMatch(self)




    def hashtagMatch(self):

        localctx = OFLCParser.HashtagMatchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_hashtagMatch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(OFLCParser.HASHTAG)
            self.state = 158
            self.cn()
            self.state = 159
            self.hashtagString()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUOTED(self):
            return self.getToken(OFLCParser.QUOTED, 0)

        def NUMBER(self):
            return self.getToken(OFLCParser.NUMBER, 0)

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(OFLCParser.WORD)
            else:
                return self.getToken(OFLCParser.WORD, i)

        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(OFLCParser.AND)
            else:
                return self.getToken(OFLCParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(OFLCParser.OR)
            else:
                return self.getToken(OFLCParser.OR, i)

        def NOT(self, i:int=None):
            if i is None:
                return self.getTokens(OFLCParser.NOT)
            else:
                return self.getToken(OFLCParser.NOT, i)

        def IN(self, i:int=None):
            if i is None:
                return self.getTokens(OFLCParser.IN)
            else:
                return self.getToken(OFLCParser.IN, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(OFLCParser.ID)
            else:
                return self.getToken(OFLCParser.ID, i)

        def HASHTAG(self, i:int=None):
            if i is None:
                return self.getTokens(OFLCParser.HASHTAG)
            else:
                return self.getToken(OFLCParser.HASHTAG, i)

        def getRuleIndex(self):
            return OFLCParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)




    def string(self):

        localctx = OFLCParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.match(OFLCParser.QUOTED)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.match(OFLCParser.NUMBER)
                pass
            elif token in [10, 11, 12, 13, 15, 16, 19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 163
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 637952) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 170
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 164
                        self.match(OFLCParser.T__0)
                        self.state = 166
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                        if la_ == 1:
                            self.state = 165
                            _la = self._input.LA(1)
                            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 637952) != 0)):
                                self._errHandler.recoverInline(self)
                            else:
                                self._errHandler.reportMatch(self)
                                self.consume()

                 
                    self.state = 172
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueSubStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(OFLCParser.StringContext,0)


        def WILDCARD(self, i:int=None):
            if i is None:
                return self.getTokens(OFLCParser.WILDCARD)
            else:
                return self.getToken(OFLCParser.WILDCARD, i)

        def getRuleIndex(self):
            return OFLCParser.RULE_valueSubString

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValueSubString" ):
                listener.enterValueSubString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValueSubString" ):
                listener.exitValueSubString(self)




    def valueSubString(self):

        localctx = OFLCParser.ValueSubStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_valueSubString)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 175
                self.match(OFLCParser.WILDCARD)


            self.state = 178
            self.string()
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 179
                self.match(OFLCParser.WILDCARD)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HashtagStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(OFLCParser.WORD, 0)

        def string(self):
            return self.getTypedRuleContext(OFLCParser.StringContext,0)


        def getRuleIndex(self):
            return OFLCParser.RULE_hashtagString

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHashtagString" ):
                listener.enterHashtagString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHashtagString" ):
                listener.exitHashtagString(self)




    def hashtagString(self):

        localctx = OFLCParser.HashtagStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_hashtagString)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(OFLCParser.T__1)
                self.state = 183
                self.match(OFLCParser.WORD)
                pass
            elif token in [10, 11, 12, 13, 15, 16, 17, 19, 20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.string()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(OFLCParser.AND, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(OFLCParser.WS)
            else:
                return self.getToken(OFLCParser.WS, i)

        def getRuleIndex(self):
            return OFLCParser.RULE_and

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)




    def and_(self):

        localctx = OFLCParser.AndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_and)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 187
                self.match(OFLCParser.WS)


            self.state = 190
            self.match(OFLCParser.AND)
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 191
                self.match(OFLCParser.WS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OR(self):
            return self.getToken(OFLCParser.OR, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(OFLCParser.WS)
            else:
                return self.getToken(OFLCParser.WS, i)

        def getRuleIndex(self):
            return OFLCParser.RULE_or

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)




    def or_(self):

        localctx = OFLCParser.OrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_or)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 194
                self.match(OFLCParser.WS)


            self.state = 197
            self.match(OFLCParser.OR)
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 198
                self.match(OFLCParser.WS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(OFLCParser.NOT, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(OFLCParser.WS)
            else:
                return self.getToken(OFLCParser.WS, i)

        def getRuleIndex(self):
            return OFLCParser.RULE_not

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot" ):
                listener.enterNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot" ):
                listener.exitNot(self)




    def not_(self):

        localctx = OFLCParser.NotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_not)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 201
                self.match(OFLCParser.WS)


            self.state = 204
            self.match(OFLCParser.NOT)
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 205
                self.match(OFLCParser.WS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IN(self):
            return self.getToken(OFLCParser.IN, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(OFLCParser.WS)
            else:
                return self.getToken(OFLCParser.WS, i)

        def getRuleIndex(self):
            return OFLCParser.RULE_in

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIn" ):
                listener.enterIn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIn" ):
                listener.exitIn(self)




    def in_(self):

        localctx = OFLCParser.InContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_in)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 208
                self.match(OFLCParser.WS)


            self.state = 211
            self.match(OFLCParser.IN)
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 212
                self.match(OFLCParser.WS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(OFLCParser.WS)
            else:
                return self.getToken(OFLCParser.WS, i)

        def getRuleIndex(self):
            return OFLCParser.RULE_eq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEq" ):
                listener.enterEq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEq" ):
                listener.exitEq(self)




    def eq(self):

        localctx = OFLCParser.EqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_eq)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 215
                self.match(OFLCParser.WS)


            self.state = 218
            self.match(OFLCParser.T__2)
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 219
                self.match(OFLCParser.WS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(OFLCParser.WS)
            else:
                return self.getToken(OFLCParser.WS, i)

        def getRuleIndex(self):
            return OFLCParser.RULE_ne

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNe" ):
                listener.enterNe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNe" ):
                listener.exitNe(self)




    def ne(self):

        localctx = OFLCParser.NeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_ne)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 222
                self.match(OFLCParser.WS)


            self.state = 225
            self.match(OFLCParser.T__3)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 226
                self.match(OFLCParser.WS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(OFLCParser.WS)
            else:
                return self.getToken(OFLCParser.WS, i)

        def getRuleIndex(self):
            return OFLCParser.RULE_po

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPo" ):
                listener.enterPo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPo" ):
                listener.exitPo(self)




    def po(self):

        localctx = OFLCParser.PoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_po)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 229
                self.match(OFLCParser.WS)


            self.state = 232
            self.match(OFLCParser.T__4)
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 233
                self.match(OFLCParser.WS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(OFLCParser.WS)
            else:
                return self.getToken(OFLCParser.WS, i)

        def getRuleIndex(self):
            return OFLCParser.RULE_pc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPc" ):
                listener.enterPc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPc" ):
                listener.exitPc(self)




    def pc(self):

        localctx = OFLCParser.PcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_pc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 236
                self.match(OFLCParser.WS)


            self.state = 239
            self.match(OFLCParser.T__5)
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 240
                self.match(OFLCParser.WS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(OFLCParser.WS)
            else:
                return self.getToken(OFLCParser.WS, i)

        def getRuleIndex(self):
            return OFLCParser.RULE_co

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCo" ):
                listener.enterCo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCo" ):
                listener.exitCo(self)




    def co(self):

        localctx = OFLCParser.CoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_co)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 243
                self.match(OFLCParser.WS)


            self.state = 246
            self.match(OFLCParser.T__6)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 247
                self.match(OFLCParser.WS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(OFLCParser.WS)
            else:
                return self.getToken(OFLCParser.WS, i)

        def getRuleIndex(self):
            return OFLCParser.RULE_dd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDd" ):
                listener.enterDd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDd" ):
                listener.exitDd(self)




    def dd(self):

        localctx = OFLCParser.DdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_dd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 250
                self.match(OFLCParser.WS)


            self.state = 253
            self.match(OFLCParser.T__7)
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 254
                self.match(OFLCParser.WS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(OFLCParser.WS)
            else:
                return self.getToken(OFLCParser.WS, i)

        def getRuleIndex(self):
            return OFLCParser.RULE_cn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCn" ):
                listener.enterCn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCn" ):
                listener.exitCn(self)




    def cn(self):

        localctx = OFLCParser.CnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_cn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 257
                self.match(OFLCParser.WS)


            self.state = 260
            self.match(OFLCParser.T__0)
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 261
                self.match(OFLCParser.WS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(OFLCParser.WS)
            else:
                return self.getToken(OFLCParser.WS, i)

        def getRuleIndex(self):
            return OFLCParser.RULE_tl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTl" ):
                listener.enterTl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTl" ):
                listener.exitTl(self)




    def tl(self):

        localctx = OFLCParser.TlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_tl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 264
                self.match(OFLCParser.WS)


            self.state = 267
            self.match(OFLCParser.T__8)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 268
                self.match(OFLCParser.WS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_intContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def po(self):
            return self.getTypedRuleContext(OFLCParser.PoContext,0)


        def pc(self):
            return self.getTypedRuleContext(OFLCParser.PcContext,0)


        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(OFLCParser.NUMBER)
            else:
                return self.getToken(OFLCParser.NUMBER, i)

        def dd(self):
            return self.getTypedRuleContext(OFLCParser.DdContext,0)


        def getRuleIndex(self):
            return OFLCParser.RULE_range_int

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange_int" ):
                listener.enterRange_int(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange_int" ):
                listener.exitRange_int(self)




    def range_int(self):

        localctx = OFLCParser.Range_intContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_range_int)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.po()
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 272
                self.match(OFLCParser.NUMBER)
                self.state = 273
                self.dd()
                self.state = 274
                self.match(OFLCParser.NUMBER)
                pass

            elif la_ == 2:
                self.state = 276
                self.dd()
                self.state = 277
                self.match(OFLCParser.NUMBER)
                pass

            elif la_ == 3:
                self.state = 279
                self.match(OFLCParser.NUMBER)
                self.state = 280
                self.dd()
                pass


            self.state = 283
            self.pc()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         




