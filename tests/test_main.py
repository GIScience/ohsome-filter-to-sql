import sqlite3

import pytest
from pytest_approval import verify

from ohsome_filter_to_sql.main import build_tree, main


def validate(query: str):
    con = sqlite3.connect(":memory:")
    try:
        con.execute(query)
    except sqlite3.OperationalError as error:
        if "syntax error" in str(error):
            raise AssertionError("Syntax error in SQL query") from error  # noqa: TRY003


@pytest.mark.parametrize(
    "filter",
    (
        "natural=tree",
        "type:node and natural=tree",
        "id:(node/1, way/2) and type:way",
    ),
)
def test_build_tree(filter):
    tree = build_tree(filter).toStringTree()
    assert verify(tree)


@pytest.mark.parametrize(
    "filter",
    (
        "natural=tree",  #      tagMatch
        '"type"=boundary',  #   tagMatch w/ keyword as key
        'name="other"',  #      tagMatch w/ keyword as value
        "natural=*",  #         tagWildcardMatch
        "oneway!=yes",  #       tagNotMatch
        "name!=*"  #            tagNotWildcardMatch
        "highway in (residential, living_street)",  # tagListMatch
        '"type" in (boundary, route)',  #       tagListMatch w/keyword as key
        "highway in (residential, other)",  #   tagListMatch w/keyword unquoted as value
        "natural in (residential)",  #          tagListMatch w/keyword with single value
    ),
)
def test_tag_match(filter):
    query = main(filter)
    assert verify(query)
    validate("SELECT * FROM foo WHERE " + query)


def test_expression_and_expression():
    filter = "natural=tree and power=plant"
    query = main(filter)
    assert verify(query)
    validate("SELECT * FROM foo WHERE " + query)


def test_expression_or_expression():
    filter = "natural=tree or power=plant"
    query = main(filter)
    assert verify(query)
    validate("SELECT * FROM foo WHERE " + query)


@pytest.mark.parametrize(
    "filter",
    (
        "(natural=tree)",
        '("type"=boundary or name="other") and natural=tree',
    ),
)
def test_expression_in_brakets(filter):
    query = main(filter)
    assert verify(query)
    validate("SELECT * FROM foo WHERE " + query)


@pytest.mark.parametrize(
    "filter",
    (
        "type:node",
        "type:way",
        "type:relation",
    ),
)
def test_type_match(filter):
    query = main(filter)
    assert verify(query)
    validate("SELECT * FROM foo WHERE " + query)


def test_id_match():
    filter = "id:3644187633"
    query = main(filter)
    assert verify(query)
    validate("SELECT * FROM foo WHERE " + query)


@pytest.mark.parametrize(
    "filter",
    (
        "id:node/3644187633",
        "id:way/3644187633",
        "id:relation/3644187633",
    ),
)
def test_type_id_match(filter):
    query = main(filter)
    assert verify(query)
    validate("SELECT * FROM foo WHERE " + query)


@pytest.mark.parametrize(
    "filter",
    (
        "id:(1..9999)",
        "id:(..9999)",
        "id:(1..)",
    ),
)
def test_id_range_match(filter):
    query = main(filter)
    assert verify(query)
    validate("SELECT * FROM foo WHERE " + query)


@pytest.mark.parametrize(
    "filter",
    (
        "id:(1)",
        "id:(1, 42, 1234)",
    ),
)
def test_id_list_match(filter):
    query = main(filter)
    assert verify(query)
    validate("SELECT * FROM foo WHERE " + query)


@pytest.mark.parametrize(
    "filter",
    (
        "id:(node/1)",
        "id:(node/1, way/42, relation/1234)",
    ),
)
def test_type_id_list_match(filter):
    query = main(filter)
    assert verify(query)
    validate("SELECT * FROM foo WHERE " + query)
