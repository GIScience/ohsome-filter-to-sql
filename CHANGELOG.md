# Changelog

## 0.4.0

### Feature

- Introduce parameter to shift numbered query args by desired int (#f903e97)
    - args_shift: Integer by which to shift numbered query arguments: $n + arg_shift
- Make public function directly importable from ohsome_filter_to_sql instead of
  ohsome_filter_to_sql.main (#469d024)

## 0.3.0

### Feature

- add validation function (`validate_filter`) and a type alias using validation
  function via pydantic validator pattern (`OhsomeFilter`) (#d6894f3)

## 0.2.0

### Breaking Changes

- Return query and query parameter separately instead
    - Output query and query parameter separately to avoid SQL injection.
    - Use query parameter syntax of Postgres, which is supported by asyncpg.
