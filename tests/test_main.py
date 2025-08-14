from typing import AsyncGenerator

import asyncpg
import pytest
import pytest_asyncio
from asyncpg import Record
from asyncpg.connection import Connection
from pytest_approval import verify

from ohsome_filter_to_sql.main import build_tree, ohsome_filter_to_sql

pytestmark = pytest.mark.asyncio  # mark all tests


async def validate_and_verify(
    db_con: Connection,
    sql_where_clause: str,
    filter: str,
):
    """Validate query and verify results.

    Build SQL query from given WHERE Clause.
    Run SQL query against a real database.
    Verify SQL query results through approval testing.
    """
    sql = "SELECT COUNT(*) FROM contributions WHERE " + sql_where_clause
    results: list[Record] = await db_con.fetch(sql)
    text = "\n\n".join([filter, sql_where_clause, str(results)])
    return verify(text)


@pytest_asyncio.fixture(scope="session")
async def db_con() -> AsyncGenerator[Connection, None]:
    con = await asyncpg.connect(
        user="postgres",
        password="mylocalpassword",  # noqa: S106
        host="localhost",
        port=5432,
    )
    yield con
    await con.close()


@pytest.mark.parametrize(
    "filter",
    (
        "natural=tree",
        "type:node and natural=tree",
        "id:(node/1, way/2) and type:way",
    ),
)
async def test_build_tree(filter):
    tree = build_tree(filter).toStringTree()
    assert verify(tree)


# -- Tests are sorted in the same order as rules in OFL.g4
#


async def test_expression_and_expression(db_con):
    filter = "natural=tree and leaf_type=broadleaved"
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(db_con, sql, filter)


async def test_expression_or_expression(db_con):
    filter = "natural=tree or leaf_type=broadleaved"
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(db_con, sql, filter)


@pytest.mark.parametrize(
    "filter",
    (
        "(natural=tree)",
        '("addr:housenumber"=45 and "addr:street"="Berliner Straße") or name="HeiGIT"',
    ),
)
async def test_expression_in_brakets(db_con, filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(db_con, sql, filter)


@pytest.mark.skip("Not implemented yet.")
async def test_hashtag_match(db_con):
    filter = "hashtag:missingmaps"
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(db_con, sql, filter)


@pytest.mark.skip("Not implemented yet.")
@pytest.mark.parametrize(
    "filter",
    (
        "hashtag:(missingmaps)",
        "hashtag:(missingmaps, type, other)",
    ),
)
async def test_hashtag_list_match(db_con, filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(db_con, sql, filter)


# TODO
# add tests for all grammar keywords like number, geometry, id, ...
@pytest.mark.parametrize(
    "filter",
    (
        '"addr:housenumber"="45"',  # tagMatch
        "natural=tree",  #      tagMatch
        '"type"=boundary',  #   tagMatch w/ keyword as key
        '"building:material"="other"',  #      tagMatch w/ keyword as value
        "natural=*",  #         tagWildcardMatch
        "oneway!=yes",  #       tagNotMatch
        "name!=*",  #            tagNotWildcardMatch
        "highway in (residential, living_street)",  # tagListMatch
        '"type" in (boundary, route)',  #             tagListMatch w/keyword as key
        "highway in (residential, other)",  #   tagListMatch w/keyword unquoted as value
        "natural in (water)",  #                tagListMatch w/keyword with single value
        '"*"=*',
    ),
)
async def test_tag_match(db_con, filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(db_con, sql, filter)


@pytest.mark.parametrize(
    "filter",
    (
        "type:node",
        "type:way",
        "type:relation",
    ),
)
async def test_type_match(db_con, filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(db_con, sql, filter)


async def test_id_match(db_con):
    filter = "id:4540889804"
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(db_con, sql, filter)


@pytest.mark.parametrize(
    "filter",
    (
        "id:node/4540889804",
        "id:way/1136431018",
        "id:relation/2070281",
    ),
)
async def test_type_id_match(db_con, filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(db_con, sql, filter)


@pytest.mark.parametrize(
    "filter",
    (
        "id:(1..9999)",
        "id:(..9999)",
        "id:(1..)",
    ),
)
async def test_id_range_match(db_con, filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(db_con, sql, filter)


@pytest.mark.parametrize(
    "filter",
    (
        "id:(4540889804)",
        "id:(1136431018, 4540889804, 2070281)",
    ),
)
async def test_id_list_match(db_con, filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(db_con, sql, filter)


@pytest.mark.parametrize(
    "filter",
    (
        "id:(node/4540889804)",
        "id:(node/4540889804, way/1136431018, relation/2070281)",
    ),
)
async def test_type_id_list_match(db_con, filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(db_con, sql, filter)


@pytest.mark.parametrize(
    "filter",
    (
        "geometry:point",
        "geometry:line",
        "geometry:polygon",
    ),
)
async def test_geometry_match(db_con, filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(db_con, sql, filter)


@pytest.mark.skip("Not implemented yet.")
async def test_geometry_match_other(db_con, filter):
    filter = "geometry:other"
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(db_con, sql, filter)


@pytest.mark.parametrize(
    "filter",
    (
        "area:(1.0..1E6)",
        "area:(1.3..)",
        "area:(2.0..1.0)",
        "area:(1e6..)",
        "area:(1..1e6)",
    ),
)
async def test_area_range_match(db_con, filter):
    # TODO: ValueError: not enough values to unpack (expected 2, got 1)
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(db_con, sql, filter)


@pytest.mark.parametrize(
    "filter",
    (
        "length:(1.0..99.99)",
        "length:(1E6..)",
        "length:(1e6..)",
        "length:(..10000)",
    ),
)
async def test_length_range_match(db_con, filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(db_con, sql, filter)


@pytest.mark.skip("Not implemented yet.")
async def test_changeset_match(db_con):
    filter = "changeset:1"
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(db_con, sql, filter)


@pytest.mark.skip("Not implemented yet.")
@pytest.mark.parametrize(
    "filter",
    (
        "changeset:(1)",
        "changeset:(1, 300, 4264)",
    ),
)
async def test_changeset_list_match(db_con, filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(db_con, sql, filter)


@pytest.mark.skip("Not implemented yet.")
@pytest.mark.parametrize(
    "filter",
    (
        "changeset:(1..999)",
        "changeset:(1..)",
        "changeset:(..999)",
    ),
)
async def test_changeset_range_match(db_con, filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(db_con, sql, filter)


@pytest.mark.skip("Not implemented yet.")
@pytest.mark.parametrize(
    "filter",
    (
        "changeset.created_by:Potlatch",
        'changeset.created_by:"Go Map!! 4.3.0"',
        'changeset.created_by:"bulk_upload.py"',
        'changeset.created_by:"JOSM/1.5 (19253 en_GB)"',
    ),
)
async def test_changeset_created_by_match(db_con, filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(db_con, sql, filter)


@pytest.mark.parametrize(
    "filter",
    (
        "id:(1 ..2",  # missing closing bracket
        "id:(1, 2",  # missing closing bracket
        "id:(1, 2,)",  # missing closing bracket
        "area:(-1..)",
        "area:(1.0..-200)",
        "length:(..-200)",
        "*=*",
    ),
)
async def test_invalid_filters(filter):
    with pytest.raises(ValueError) as e:  # noqa: F841
        ohsome_filter_to_sql(filter)
