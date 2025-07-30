# README

## Installation

```sh
uv tool install git+https://gitlab.heigit.org/giscience/big-data/ohsome/libs/ohsome-filter-to-sql
```

You can run the CLI without installation with `uvx`:
```sh
uvx --from git+https://gitlab.heigit.org/giscience/big-data/ohsome/libs/ohsome-filter-to-sql ohsome-filter-to-sql
```

## Usage

```sh
$ ohsome-filter-to-sql  # start CLI
natural = tree  # type in ohsome filter
tags->>'natural' = 'tree'  # result
```

## Development Setup

```sh
uv run pre-commit install
uv run pytest
```

### How to play around with the grammar?

Execute `antlr4-parse`, type in an ohsome filter and press ctlr+d.

```sh
antlr4-parse OFL.g4 root -tree
buildings=yes
(root:1 (expression:8 (tagMatch:1 (string:1 buildings) = (string:1 yes))) <EOF>)
```

### How to generating parser code?

When the grammar file has change generate new Python code with `antlr4` and move genrated files to `ohsome_filter_to_sql/`.

```sh
uv run antlr4 -Dlanguage=Python3 OFL.g4
mv *.py ohsome_filter_to_sql/
```

## Previous Work

- [ohsome filter language - grammar](https://gitlab.heigit.org/giscience/big-data/ohsome/ohsome-now/ohsome-now-app/-/blob/main/backend/src/main/antlr/org/heigit/ohsome/filter/OFL.g4) by Matthias Merdes
- [ohsome filter language - grammar](https://gitlab.heigit.org/-/snippets/62) by Martin Raifer (based upon above grammar)
- [ohsome filter to SQL in Java](https://gitlab.heigit.org/martin/ohsome-filter-language-example/-/blob/main/src/main/java/org/heigit/ohsome/OhsomeFilterToSql.java?ref_type=heads) by Martin Raifer (uses above grammar)

## Resources

- [ohsome filter documentation](https://docs.ohsome.org/ohsome-api/v1/filter.html)
- [ANTLR with Python - Introduction](https://yetanotherprogrammingblog.medium.com/antlr-with-python-974c756bdb1b)
- [ANTLR Listeners](https://github.com/antlr/antlr4/blob/master/doc/listeners.md)
