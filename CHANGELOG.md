# Changelog

## Current Main

### Feature

- add validation function (`validate_filter`) and a type alias using validation
  function via pydantic validator pattern (`OhsomeFilter`) (d6894f3)

## 0.2.0

### Breaking Changes

- Return query and query parameter separately instead
    - Output query and query parameter separately to avoid SQL injection.
    - Use query parameter syntax of Postgres, which is supported by asyncpg.
