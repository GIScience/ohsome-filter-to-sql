# ohsome filter to SQL

[![Build Status](https://jenkins.heigit.org/buildStatus/icon?job=ohsome-filter/main)](https://jenkins.heigit.org/job/ohsome-filter/job/main/)
[![PyPI - Version](https://img.shields.io/pypi/v/ohsome-filter-to-sql)](https://pypi.org/project/ohsome-filter-to-sql/)
[![LICENSE](https://img.shields.io/github/license/GIScience/ohsome-filter-to-sql)](COPYING)
[![status: active](https://github.com/GIScience/badges/raw/master/status/active.svg)](https://github.com/GIScience/badges#active)

## Documentation

Please see the section on the [ohsome filter](https://docs.ohsome.org/ohsome-api/v2-rc/reference/filter.html) in the ohsome API documentation.

## Try it out

```sh
# USAGE:
#   after running ohsome-filter-to-sql type in ohsome filter and hit enter
$ uvx ohsome-filter-to-sql
natural = tree and leaftype = broadleaf
('tags @> $1 AND tags @> $2', ('{"natural": "tree"}', '{"leaftype": "broadleaf"}'))
```

## Installation

```sh
uv add ohsome-filter-to-sql
```

## Usage

### Python Library

To generate the SQL WHERE clause (`query`) alongside its query arguments:

```python
from ohsome_filter_to_sql import ohsome_filter_to_sql

query, query_args = ohsome_filter_to_sql("natural = tree")
```

The generated SQL WHERE clause contains native PostgresSQL syntax for query arguments: `$n`.

`ohsome-filter-to-sql` can also be used to validate a give ohsome filter in Python:

```python
from ohsome_filter_to_sql import validate_filter, ParserValueError

validate_filter("natural = tree")
try:
    validate_filter("geometry:foo")
except ParserValueError:
    pass
```

Alternatively, ohsome filter can be validated during runtime with Pydantic:

```python
from ohsome_filter_to_sql import OhsomeFilter
from pydantic import validate_call


@validate_call
def request(ohsome_filter: OhsomeFilter):
    pass
```

### Command Line Interface (CLI)

```sh
uv run ohsome-filter-to-sql
```

## Development Setup

```sh
uv run prek install  # pre-commit hooks

export OHSOME_FILTER_TO_SQL_SCHEMA=""
export OHSOME_FILTER_TO_SQL_DATABASE=""
export OHSOME_FILTER_TO_SQL_USER=""
export OHSOME_FILTER_TO_SQL_PASSWORD=""
export OHSOME_FILTER_TO_SQL_HOST="localhost"
export OHSOME_FILTER_TO_SQL_PORT="5432"
uv run pytest
```

To develop new features you will need access to the ohsomeDB in production or a local instance of the [ohsomeDB](https://gitlab.heigit.org/giscience/big-data/ohsome/ohsomedb/ohsomedb/-/tree/main/local_setup).


### How to play around with the grammar?

Execute `antlr4-parse`, type in an ohsome filter and press ctlr+d.

```sh
antlr4-parse OFL.g4 root -tree
buildings=yes
(root:1 (expression:8 (tagMatch:1 (string:1 buildings) = (string:1 yes))) <EOF>)
```

[ANTLR Lab](http://lab.antlr.org/) can also be used to try out the grammar.


### How to generate the parser code?

When the grammar file has changed generate new Python code with `antlr4` and move generated files to `ohsome_filter_to_sql/`.

```sh
export ANTLR4_TOOLS_ANTLR_VERSION=$(uv pip show antlr4-python3-runtime | awk '/^Version:/{print $2}')
uv run antlr4 -Dlanguage=Python3 OFL.g4 && mv *.py ohsome_filter_to_sql/
```

### Release

This project uses [SemVer](https://semver.org/).

To make a new release run `./scripts/release.sh <version number>`.


## Resources

- [ohsome filter documentation](https://docs.ohsome.org/ohsome-api)
- [ANTLR with Python - Introduction](https://yetanotherprogrammingblog.medium.com/antlr-with-python-974c756bdb1b)
- [ANTLR Listeners](https://github.com/antlr/antlr4/blob/master/doc/listeners.md)
- [ohsomeDB schema](https://gitlab.heigit.org/giscience/big-data/ohsome/ohsomedb/ohsomedb/-/blob/main/create-schema.sql)
