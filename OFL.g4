grammar OFL;


root: WS* expression? WS* EOF;

expression
  : po expression pc
  | not expression
  | expression and expression
  | expression or expression

  | hashtagMatch
  | hashtagWildcardMatch
  | hashtagListMatch

  | tagMatch
  | tagWildcardMatch
  | tagNotMatch
  | tagNotWildcardMatch
  | tagListMatch
  | tagValuePatternMatch

  | typeMatch
  | idMatch
  | typeIdMatch
  | idRangeMatch
  | idListMatch
  | typeIdListMatch

  | geometryMatch
  | areaRangeMatch
  | perimeterRangeMatch
  | lengthRangeMatch
  | geometryVerticesRangeMatch
  | geometryOutersMatch
  | geometryOutersRangeMatch
  | geometryInnersMatch
  | geometryInnersRangeMatch

  | changesetMatch
  | changesetListMatch
  | changesetRangeMatch
  | changesetCreatedByMatch;


tagMatch: string eq string;
tagWildcardMatch: string eq WILDCARD;
tagListMatch: string in po string (co string)* pc;
tagNotMatch: string ne string;
tagNotWildcardMatch: string ne WILDCARD;
tagValuePatternMatch: string tl valueSubString;

hashtagMatch: HASHTAG cn string;
hashtagWildcardMatch: HASHTAG cn WORD WILDCARD;
hashtagListMatch: HASHTAG cn po string (co string)* pc;

typeMatch: TYPE cn OSMTYPE;
idMatch: ID cn NUMBER;
typeIdMatch: ID cn OSMID;
idRangeMatch: ID cn range_int;
idListMatch: ID cn po NUMBER (co NUMBER)* pc;
typeIdListMatch: ID cn po OSMID (co OSMID)* pc;

geometryMatch: GEOMETRY cn GEOMETRY_TYPE;
areaRangeMatch: AREA cn range_dec;
perimeterRangeMatch: PERIMETER cn range_dec;
lengthRangeMatch: LENGTH cn range_dec;
geometryVerticesRangeMatch: GEOMETRY_VERTICES cn range_int;
geometryOutersMatch: GEOMETRY_OUTERS cn NUMBER;
geometryOutersRangeMatch: GEOMETRY_OUTERS cn range_int;
geometryInnersMatch: GEOMETRY_INNERS cn NUMBER;
geometryInnersRangeMatch: GEOMETRY_INNERS cn range_int;

changesetMatch: CHANGESET cn NUMBER;
changesetListMatch: CHANGESET cn po NUMBER (co NUMBER)* pc;
changesetRangeMatch: CHANGESET cn range_int;
changesetCreatedByMatch: CHANGESET_CREATEDBY cn string;


string
  : QUOTED
  | NUMBER
  | (    (WORD | AND | OR | NOT | IN | TYPE | ID | GEOMETRY | AREA | PERIMETER | LENGTH | GEOMETRY_VERTICES | GEOMETRY_OUTERS | GEOMETRY_INNERS | CHANGESET | CHANGESET_CREATEDBY | HASHTAG | OSMTYPE | GEOMETRY_TYPE)
    (':' (WORD | AND | OR | NOT | IN | TYPE | ID | GEOMETRY | AREA | PERIMETER | LENGTH | GEOMETRY_VERTICES | GEOMETRY_OUTERS | GEOMETRY_INNERS | CHANGESET | CHANGESET_CREATEDBY | HASHTAG | OSMTYPE | GEOMETRY_TYPE)?)*);
valueSubString: WILDCARD? string WILDCARD?;


AND: 'and';
OR: 'or';
NOT: 'not';
IN: 'in';

and: WS* AND WS*;
or: WS* OR WS*;
not: WS* NOT WS*;
in : WS* IN WS*;

eq: WS* '=' WS*;
ne: WS* '!=' WS*;
po: WS* '(' WS*;
pc: WS* ')' WS*;
co: WS* ',' WS*;
dd: WS* '..' WS*;
cn: WS* ':' WS*;
tl: WS* '~' WS*;

WILDCARD: '*';

TYPE: 'type';
ID: 'id';
GEOMETRY: 'geometry';
AREA: 'area';
PERIMETER: 'perimeter';
LENGTH: 'length';
GEOMETRY_VERTICES: 'geometry.vertices';
GEOMETRY_OUTERS: 'geometry.outers';
GEOMETRY_INNERS: 'geometry.inners';
CHANGESET: 'changeset';
CHANGESET_CREATEDBY: 'changeset.created_by';
HASHTAG: 'hashtag';

OSMTYPE: 'node' | 'way' | 'relation';
OSMID: OSMTYPE '/' NUMBER;
GEOMETRY_TYPE: 'point' | 'line' | 'polygon' | 'other';

NUMBER: NUMERAL+;
DECIMAL: NUMERAL+ ('.' NUMERAL+)? ([Ee] NUMERAL+)?;
WORD: LETTER+;
QUOTED: '"' CHARACTER+ '"';

range_int: po (NUMBER dd NUMBER | dd NUMBER | NUMBER dd ) pc;
range_dec: po ((NUMBER | DECIMAL) dd (NUMBER | DECIMAL) | dd (NUMBER | DECIMAL) | (NUMBER | DECIMAL) dd) pc;

COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\n\r]* ('\r'? '\n' | EOF) -> skip;
WS: [ \t\r\n];

fragment NUMERAL: [0-9];
fragment LETTER: [-_a-zA-Z0-9];
fragment CHARACTER: ~["\\\r\n] | ESCAPE_SEQUENCE;
fragment ESCAPE_SEQUENCE: '\\' ["rn\\];