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

Can we re-write or queries to not use or but a json operator?
