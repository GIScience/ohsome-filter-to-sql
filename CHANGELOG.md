# Changelog

## Main

* build: upgrade pytest to 9.x (f7410de)
* build: upgrade dependencies (15f9694)
* build: remove deprecated license classifier (a409fe4)
* build: bump uv_build to <0.12 (f9d8325)
* build: move dependencies which are only used for test to dev group (d27c796)

## Release 0.8.0

### Feature

* support python version 3.14 (c794c02)

### Development

* tests: recreate cassettes and approvals after bump of python version (dcd665d)
* build(ci): run tests against two python versions (current and 3.11) (7896cfa)
* build(ci): separate static analysis stage from test stage (e070f0b)
* build: add ty as static type checker for development (e705144)
* build/tests: add pytest-randomly to run tests in random order (#033de35)
* build: migrate pre-commit hooks to prek (9f3ded3)

## 0.5.0

- build: run uv sync --upgrade to upgrade dependencies (#52a4d21)

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
