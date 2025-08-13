import asyncpg
import pytest
from pytest_approval import verify

from ohsome_filter_to_sql.main import build_tree, ohsome_filter_to_sql

pytestmark = pytest.mark.asyncio

# connection will be closed by pytest sessionfinish hook in conftest
db_con: asyncpg.connection.Connection | None = None


async def query(where_clause: str) -> str:
    """Build a count SQL query, query database. Returned formatted SQL and results."""
    global db_con
    if db_con is None:
        db_con = await asyncpg.connect(
            user="postgres",
            password="mylocalpassword",  # noqa: S106
            host="localhost",
            port=5432,
        )
    sql = "SELECT COUNT(*) FROM contributions WHERE " + where_clause
    results: list[asyncpg.Record] = await db_con.fetch(sql)
    return format_sql(sql) + "\n\n" + str(results)


def format_sql(_):
    """Make SQL string pretty."""
    _ = _.split("FROM")
    _ = "\nFROM".join(_)

    _ = _.split("WHERE")
    _ = "\nWHERE".join(_)

    _ = _.split("AND")
    _ = "\nAND".join(_)

    _ = _.split("OR")
    _ = "\nOR".join(_)

    return _


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


async def test_expression_and_expression():
    filter = "natural=tree and leaf_type=broadleaved"
    sql = ohsome_filter_to_sql(filter)
    assert verify(sql)
    assert verify(await query(sql))


async def test_expression_or_expression():
    filter = "natural=tree or leaf_type=broadleaved"
    sql = ohsome_filter_to_sql(filter)
    assert verify(sql)
    assert verify(await query(sql))


@pytest.mark.parametrize(
    "filter",
    (
        "(natural=tree)",
        '("type"=boundary or name="other") and natural=tree',
    ),
)
async def test_expression_in_brakets(filter):
    sql = ohsome_filter_to_sql(filter)
    assert verify(sql)
    assert verify(await query(sql))


async def test_hashtag_match():
    filter = "hashtag:missingmaps"
    sql = ohsome_filter_to_sql(filter)
    assert verify(sql)
    assert verify(await query(sql))


@pytest.mark.parametrize(
    "filter",
    (
        "hashtag:(missingmaps)",
        "hashtag:(missingmaps, type, other)",
    ),
)
async def test_hashtag_list_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert verify(sql)
    assert verify(await query(sql))


@pytest.mark.parametrize(
    "filter",
    (
        '"addr:housenumber"="45"',  # tagMatch
        "natural=tree",  #      tagMatch
        '"type"=boundary',  #   tagMatch w/ keyword as key
        'name="other"',  #      tagMatch w/ keyword as value
        "natural=*",  #         tagWildcardMatch
        "oneway!=yes",  #       tagNotMatch
        "name!=*"  #            tagNotWildcardMatch
        "highway in (residential, living_street)",  # tagListMatch
        '"type" in (boundary, route)',  #             tagListMatch w/keyword as key
        "highway in (residential, other)",  #   tagListMatch w/keyword unquoted as value
        "natural in (water)",  #                tagListMatch w/keyword with single value
    ),
)
async def test_tag_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert verify(sql)
    assert verify(await query(sql))


@pytest.mark.parametrize(
    "filter",
    (
        "type:node",
        "type:way",
        "type:relation",
    ),
)
async def test_type_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert verify(sql)
    assert verify(await query(sql))


async def test_id_match():
    filter = "id:3644187633"
    sql = ohsome_filter_to_sql(filter)
    assert verify(sql)
    assert verify(await query(sql))


@pytest.mark.parametrize(
    "filter",
    (
        "id:node/3644187633",
        "id:way/3644187633",
        "id:relation/3644187633",
    ),
)
async def test_type_id_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert verify(sql)
    assert verify(await query(sql))


@pytest.mark.parametrize(
    "filter",
    (
        "id:(1..9999)",
        "id:(..9999)",
        "id:(1..)",
    ),
)
async def test_id_range_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert verify(sql)
    assert verify(await query(sql))


@pytest.mark.parametrize(
    "filter",
    (
        "id:(1)",
        "id:(1, 42, 1234)",
    ),
)
async def test_id_list_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert verify(sql)
    assert verify(await query(sql))


@pytest.mark.parametrize(
    "filter",
    (
        "id:(node/1)",
        "id:(node/1, way/42, relation/1234)",
    ),
)
async def test_type_id_list_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert verify(sql)
    assert verify(await query(sql))


@pytest.mark.parametrize(
    "filter",
    (
        "geometry:point",
        "geometry:line",
        "geometry:polygon",
        "geometry:other",
    ),
)
async def test_geometry_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert verify(sql)
    assert verify(await query(sql))


@pytest.mark.parametrize(
    "filter",
    (
        "area:(1.0..99.99)",
        "area:(1.0..)",
        "area:(..99.99)",
    ),
)
async def test_area_range_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert verify(sql)
    assert verify(await query(sql))


@pytest.mark.parametrize(
    "filter",
    (
        "length:(1.0..99.99)",
        "length:(1.0..)",
        "length:(..99.99)",
    ),
)
async def test_length_range_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert verify(sql)
    assert verify(await query(sql))


async def test_changeset_match():
    filter = "changeset:1"
    sql = ohsome_filter_to_sql(filter)
    assert verify(sql)
    assert verify(await query(sql))


@pytest.mark.parametrize(
    "filter",
    (
        "changeset:(1)",
        "changeset:(1, 300, 4264)",
    ),
)
async def test_changeset_list_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert verify(sql)
    assert verify(await query(sql))


@pytest.mark.parametrize(
    "filter",
    (
        "changeset:(1..999)",
        "changeset:(1..)",
        "changeset:(..999)",
    ),
)
async def test_changeset_range_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert verify(sql)
    assert verify(await query(sql))


@pytest.mark.parametrize(
    "filter",
    (
        "changeset.created_by:Potlatch",
        'changeset.created_by:"Go Map!! 4.3.0"',
        'changeset.created_by:"bulk_upload.py"',
        'changeset.created_by:"JOSM/1.5 (19253 en_GB)"',
    ),
)
async def test_changeset_created_by_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert verify(sql)
    assert verify(await query(sql))
