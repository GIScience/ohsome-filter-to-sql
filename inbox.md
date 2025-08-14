- [ ] implement the rest of ohsome api docs examples: https://docs.ohsome.org/ohsome-api/v1/filter.html#examples
- [ ] idRange: Should operator (..) and operands separated by space be valid?
  - Examples given by the ohsome API docs have spaces
- [ ] How to deal with geometryType = other?
- [ ] Currently numbers as tag value need to be quoted. Should we support unquoted numbers?
- [ ] Feature: How could we du substring queries in ohsome filter language like SQL substring
- [ ] Is `tags?'natural'` more efficient than `tags->>natural NOT NULL`?
- [ ] Is `tags@>{'natural': 'tree'}` more efficient than `tags->>'natural' = 'tree'` for tag match?
- [ ] Is `tags @> {'highway': 'primary'} or tags @> {'highway': 'secondary'}` more efficient then `tags->>highway in (primary, secondary)`?
- [ ] New feature: case insensitive queries (e.g. `leaftype=Broadleaf and leaftype=broadleaf`)
- [ ] New feature: Normalisierte werte (meter vs meile, km/h vs ...)
- [ ] Missing listener function for following rules:
    - `hashtagWildcardMatch: string '=' WILDCARD;`
    - `perimeterRangeMatch: PERIMETER ':' '(' RANGE_DEC ')';`
    - `geometryVerticesRangeMatch: GEOMETRY_VERTICES ':' '(' RANGE_INT ')';`
    - `geometryOutersMatch: GEOMETRY_OUTERS ':' NUMBER;`
    - `geometryOutersRangeMatch: GEOMETRY_OUTERS ':' '(' RANGE_INT ')';`
    - `geometryInnersMatch: GEOMETRY_INNERS ':' NUMBER;`
    - `geometryInnersRangeMatch: GEOMETRY_INNERS ':' '(' RANGE_INT ')';`
- potential enhancement: `WHERE tags @> '{"natural": "tree"}' AND tags @> '{"leaf_type": "broadleaved"}'` vs `WHERE tags @> '{"natural": "tree", "leaf_type": "broadleaved"}'`?


Can we avoid using quoted keywords like `"type"="other"`. E.g. by extending grammar with (other keywords are missing here like other and way ...):
``` 
tagMatch: key '=' value;
value: string | TYPE;
key: string | TYPE;
```


Does not work due to value being grammar keyword
```
ohsome-filter-to-sql
foo=geometry
line 1:4 no viable alternative at input 'foo=geometry'
```
Above does not work for every keyword like area, type, id, ...


Warning but works:
```
length:(..10000)
line 1:8 mismatched input '..10000' expecting RANGE_DEC
```
