grammar OFL;


root: expression? EOF;

expression
  : '(' expression ')'
  | NOT expression
  | expression AND expression
  | expression OR expression

  | hashtagMatch
  | hashtagWildcardMatch
  | hashtagListMatch

  | tagMatch
  | tagWildcardMatch
  | tagNotMatch
  | tagNotWildcardMatch
  | tagListMatch

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


tagMatch: string '=' string;
tagWildcardMatch: string '=' WILDCARD;
tagListMatch: string 'in' '(' string (',' string)* ')';
tagNotMatch: string '!=' string;
tagNotWildcardMatch: string '!=' WILDCARD;

hashtagMatch: HASHTAG ':' string;
hashtagWildcardMatch: HASHTAG ':' WORD WILDCARD;
hashtagListMatch: HASHTAG ':' '(' string (',' string)* ')';

typeMatch: TYPE ':' OSMTYPE;
idMatch: ID ':' NUMBER;
typeIdMatch: ID ':' OSMID;
idRangeMatch: ID ':' '(' range_int ')';
idListMatch: ID ':' '(' NUMBER (',' NUMBER)* ')';
typeIdListMatch: ID ':' '(' OSMID (',' OSMID)* ')';

geometryMatch: GEOMETRY ':' GEOMETRY_TYPE;
areaRangeMatch: AREA ':' '(' range_dec ')';
perimeterRangeMatch: PERIMETER ':' '(' range_dec ')';
lengthRangeMatch: LENGTH ':' '(' range_dec ')';
geometryVerticesRangeMatch: GEOMETRY_VERTICES ':' '(' range_int ')';
geometryOutersMatch: GEOMETRY_OUTERS ':' NUMBER;
geometryOutersRangeMatch: GEOMETRY_OUTERS ':' '(' range_int ')';
geometryInnersMatch: GEOMETRY_INNERS ':' NUMBER;
geometryInnersRangeMatch: GEOMETRY_INNERS ':' '(' range_int ')';

changesetMatch: CHANGESET ':' NUMBER;
changesetListMatch: CHANGESET ':' '(' NUMBER (',' NUMBER)* ')';
changesetRangeMatch: CHANGESET ':' '(' range_int ')';
changesetCreatedByMatch: CHANGESET_CREATEDBY ':' string;


string
  : QUOTED
  | NUMBER
  | (   (WORD | AND | OR | NOT | TYPE | ID | GEOMETRY | AREA | PERIMETER | LENGTH | GEOMETRY_VERTICES | GEOMETRY_OUTERS | GEOMETRY_INNERS | CHANGESET | CHANGESET_CREATEDBY | HASHTAG | OSMTYPE | GEOMETRY_TYPE)
    (':' WORD | AND | OR | NOT | TYPE | ID | GEOMETRY | AREA | PERIMETER | LENGTH | GEOMETRY_VERTICES | GEOMETRY_OUTERS | GEOMETRY_INNERS | CHANGESET | CHANGESET_CREATEDBY | HASHTAG | OSMTYPE | GEOMETRY_TYPE)*);


AND: 'and';
OR: 'or';
NOT: 'not';

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

range_int: NUMBER '..' NUMBER | '..' NUMBER | NUMBER '..';
range_dec: (NUMBER | DECIMAL) '..' (NUMBER | DECIMAL) | '..' (NUMBER | DECIMAL) | (NUMBER | DECIMAL) '..';

WHITESPACE: [ \t\r\n]+ -> skip;

fragment NUMERAL: [0-9];
fragment LETTER: [-_a-zA-Z0-9];
fragment CHARACTER: ~["\\\r\n] | EscapeSequence;
fragment EscapeSequence: '\\' ["rn\\];

