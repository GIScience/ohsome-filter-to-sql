# README

## Installation as standalone tool (CLI)

```sh
uv tool install git+https://gitlab.heigit.org/giscience/big-data/ohsome/libs/ohsome-filter-to-sql
```

You can run the CLI without installation with `uvx`:
```sh
uvx --from git+https://gitlab.heigit.org/giscience/big-data/ohsome/libs/ohsome-filter-to-sql ohsome-filter-to-sql
```

## Usage as standalone tool (CLI)

```sh
$ ohsome-filter-to-sql  # start CLI
natural = tree and leaftype = broadleaf  # type in ohsome filter and hit enter
tags @> '{"natural": "tree"}' AND tags @> '{"leaftype": "broadleaf"}'  # result
```

## Installation as Python library

```sh
uv add ohsome-filter-to-sql
```

## Usage as Python library

```python
from ohsome_filter_to_sql import ohsome_filter_to_sql


sql_query = ohsome_filter_to_sql("natural = tree")
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

## Inbox

For open tasks, please take a look at [inbox.md](inbox.md)

## Previous Work

- [ohsome filter language - grammar](https://gitlab.heigit.org/giscience/big-data/ohsome/ohsome-now/ohsome-now-app/-/blob/main/backend/src/main/antlr/org/heigit/ohsome/filter/OFL.g4) by Matthias Merdes
- [ohsome filter language - grammar](https://gitlab.heigit.org/-/snippets/62) by Martin Raifer (based upon above grammar)
- [ohsome filter to SQL in Java](https://gitlab.heigit.org/martin/ohsome-filter-language-example/-/blob/main/src/main/java/org/heigit/ohsome/OhsomeFilterToSql.java?ref_type=heads) by Martin Raifer (uses above grammar)

## Resources

- [ohsome filter documentation](https://docs.ohsome.org/ohsome-api/v1/filter.html)
- [ANTLR with Python - Introduction](https://yetanotherprogrammingblog.medium.com/antlr-with-python-974c756bdb1b)
- [ANTLR Listeners](https://github.com/antlr/antlr4/blob/master/doc/listeners.md)
- [ohsomeDB schema](https://gitlab.heigit.org/giscience/big-data/ohsome/ohsomedb/ohsomedb/-/blob/main/create-schema.sql)
