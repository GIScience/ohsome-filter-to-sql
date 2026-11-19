grammar OFLC;


root: WS? (expression | WILDCARD) WS? EOF;

expression
  : po expression pc
  | not expression
  | expression and expression
  | expression or expression

  | tagMatch
  | tagWildcardMatch
  | tagNotMatch
  | tagNotWildcardMatch
  | tagListMatch
  | tagValuePatternMatch

  | idMatch
  | idRangeMatch
  | idListMatch;


tagMatch: string eq string;
tagWildcardMatch: string eq WILDCARD;
tagListMatch: string in po string (co string)* pc;
tagNotMatch: string ne string;
tagNotWildcardMatch: string ne WILDCARD;
tagValuePatternMatch: string tl valueSubString;

idMatch: ID cn NUMBER;
idRangeMatch: ID cn range_int;
idListMatch: ID cn po NUMBER (co NUMBER)* pc;



string
  : QUOTED
  | NUMBER
  | (    (WORD | AND | OR | NOT | IN | ID )
    (':' (WORD | AND | OR | NOT | IN | ID )?)*);
valueSubString: WILDCARD? string WILDCARD?;


AND: 'and';
OR: 'or';
NOT: 'not';
IN: 'in';

and: WS? AND WS?;
or: WS? OR WS?;
not: WS? NOT WS?;
in : WS? IN WS?;

eq: WS? '=' WS?;
ne: WS? '!=' WS?;
po: WS? '(' WS?;
pc: WS? ')' WS?;
co: WS? ',' WS?;
dd: WS? '..' WS?;
cn: WS? ':' WS?;
tl: WS? '~' WS?;

WILDCARD: '*';

ID: 'id';

NUMBER: NUMERAL+;
DECIMAL: NUMERAL+ ('.' NUMERAL+)? ([Ee] NUMERAL+)?;
WORD: LETTER+;
QUOTED: '"' CHARACTER+ '"';

range_int: po (NUMBER dd NUMBER | dd NUMBER | NUMBER dd ) pc;

WS: [ \t\r\n]+;

fragment NUMERAL: [0-9];
fragment LETTER: [-_a-zA-Z0-9];
fragment CHARACTER: ~["\\\r\n] | EscapeSequence;
fragment EscapeSequence: '\\' ["rn\\];

