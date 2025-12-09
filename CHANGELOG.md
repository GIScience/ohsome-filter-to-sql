# Current Main

## Breaking Changes

- return query and query parameter separately instead
    - Output query and query parameter separately to avoid SQL injection.
    - Use query parameter syntax of Postgres, which is supported by asyncpg.
