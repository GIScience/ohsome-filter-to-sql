# ohsome filter to SQL

[![Build Status](https://jenkins.heigit.org/buildStatus/icon?job=ohsome-filter/main)](https://jenkins.heigit.org/job/ohsome-filter/job/main/)
[![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=ohsome-filter-to-sql&metric=alert_status)](https://sonarcloud.io/dashboard?id=ohsome-filter-to-sql)
[![PyPI - Version](https://img.shields.io/pypi/v/ohsome-filter-to-sql)](https://pypi.org/project/ohsome-filter-to-sql/)
[![LICENSE](https://img.shields.io/github/license/GIScience/ohsome-filter-to-sql)](COPYING)
[![status: active](https://github.com/GIScience/badges/raw/master/status/active.svg)](https://github.com/GIScience/badges#active)

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

```python
from ohsome_filter_to_sql.main import ohsome_filter_to_sql

query, query_args = ohsome_filter_to_sql("natural = tree")
```

### Command Line Interface (CLI)

```sh
uv run ohsome-filter-to-sql
```

## Development Setup

```sh
uv run prek install  # pre-commit hooks
uv run pytest
```

To develop new features you will need a local instance of the [ohsomeDB](https://gitlab.heigit.org/giscience/big-data/ohsome/ohsomedb/ohsomedb/-/tree/main/local_setup).


### How to play around with the grammar?

Execute `antlr4-parse`, type in an ohsome filter and press ctlr+d.

```sh
antlr4-parse OFL.g4 root -tree
buildings=yes
(root:1 (expression:8 (tagMatch:1 (string:1 buildings) = (string:1 yes))) <EOF>)
```

[ANTLR Lab](http://lab.antlr.org/) can also be used to try out the grammar.


### How to generating parser code?

When the grammar file has change generate new Python code with `antlr4` and move genrated files to `ohsome_filter_to_sql/`.

```sh
uv run antlr4 -Dlanguage=Python3 OFL.g4 && mv *.py ohsome_filter_to_sql/
```


### Release

This project uses [SemVer](https://semver.org/).

To make a new release run `./scripts/release.sh <version number>`.


## Resources

- [ohsome filter documentation](https://docs.ohsome.org/ohsome-api/v1/filter.html) and [oshdb-filter](https://github.com/GIScience/oshdb/tree/main/oshdb-filter)
- [ANTLR with Python - Introduction](https://yetanotherprogrammingblog.medium.com/antlr-with-python-974c756bdb1b)
- [ANTLR Listeners](https://github.com/antlr/antlr4/blob/master/doc/listeners.md)
- [ohsomeDB schema](https://gitlab.heigit.org/giscience/big-data/ohsome/ohsomedb/ohsomedb/-/blob/main/create-schema.sql)
