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
        '"natural:addr"=tree',  #      tagMatch
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
    # validate("SELECT * FROM foo WHERE " + query)


def test_expression_and_expression():
    filter = "natural=tree and leaf_type=broadleaved"
    query = main(filter)
    assert verify(query)
    validate("SELECT * FROM foo WHERE " + query)


def test_expression_or_expression():
    filter = "natural=tree or leaf_type=broadleaved"
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


def test_hashtag_match():
    filter = "hashtag:missingmaps"
    query = main(filter)
    assert verify(query)
    validate("SELECT * FROM foo WHERE " + query)


@pytest.mark.parametrize(
    "filter",
    (
        "hashtag:(missingmaps)",
        "hashtag:(missingmaps, type, other)",
    ),
)
def test_hashtag_list_match(filter):
    query = main(filter)
    assert verify(query)
    # TODO: Validate query. Blocker: array[] is not valid sqlite syntax


def test_changeset_match():
    filter = "changeset:1"
    query = main(filter)
    assert verify(query)
    validate("SELECT * FROM foo WHERE " + query)


@pytest.mark.parametrize(
    "filter",
    (
        "changeset:(1)",
        "changeset:(1, 300, 4264l)",
    ),
)
def test_changeset_list_match(filter):
    query = main(filter)
    assert verify(query)
    validate("SELECT * FROM foo WHERE " + query)


@pytest.mark.parametrize(
    "filter",
    (
        "changeset:(1..999)",
        "changeset:(1..)",
        "changeset:(..999)",
    ),
)
def test_changeset_range_match(filter):
    query = main(filter)
    assert verify(query)
    validate("SELECT * FROM foo WHERE " + query)


@pytest.mark.parametrize(
    "filter",
    (
        "changeset.created_by:Potlatch",
        'changeset.created_by:"Go Map!! 4.3.0"',
        'changeset.created_by:"bulk_upload.py"',
        'changeset.created_by:"JOSM/1.5 (19253 en_GB)"',
    ),
)
def test_changeset_created_by_match(filter):
    query = main(filter)
    assert verify(query)


@pytest.mark.parametrize(
    "filter",
    (
        "geometry:point",
        "geometry:line",
        "geometry:polygon",
        "geometry:other",
    ),
)
def test_geometry_match(filter):
    query = main(filter)
    assert verify(query)
    validate("SELECT * FROM foo WHERE " + query)


@pytest.mark.parametrize(
    "filter",
    (
        "area:(1.0..99.99)",
        "area:(1.0..)",
        "area:(..99.99)",
    ),
)
def test_area_range_match(filter):
    query = main(filter)
    assert verify(query)
    validate("SELECT * FROM foo WHERE " + query)


@pytest.mark.parametrize(
    "filter",
    (
        "length:(1.0..99.99)",
        "length:(1.0..)",
        "length:(..99.99)",
    ),
)
def test_length_range_match(filter):
    query = main(filter)
    assert verify(query)
    validate("SELECT * FROM foo WHERE " + query)
