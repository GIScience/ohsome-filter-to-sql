# Test fixtures cover examples of the ohsome API filter documentation and
# tests fixtures used by the ohsome dashboard for ohsome filter syntax highlighting:
# - https://docs.ohsome.org/ohsome-api/v1/filter.html
# - https://github.com/GIScience/ohsome-dashboard/blob/main/src/prism-language-ohsome-filter.ts


import asyncpg
import asyncpg_recorder
import pytest
from asyncpg import Record
from pytest_approval import verify

from ohsome_filter_to_sql.main import (
    LexerValueError,
    ParserValueError,
    build_tree,
    ohsome_filter_to_sql,
    unescape,
)

pytestmark = pytest.mark.asyncio  # mark all tests


async def validate_and_verify(sql_where_clause: str, filter: str):
    """Validate query and verify results.

    Build SQL query from given WHERE Clause.
    Run SQL query against a real database.
    Verify SQL query results through approval testing.
    """
    sql = "SELECT COUNT(*) FROM contributions WHERE " + sql_where_clause
    results: list[Record] = await execute_query(sql)
    text = "\n\n".join([filter, sql_where_clause, str(results)])
    return verify(text)


@asyncpg_recorder.use_cassette
async def execute_query(sql: str) -> list[Record]:
    con = await asyncpg.connect(
        user="postgres",
        password="mylocalpassword",  # noqa: S106
        host="localhost",
        port=5432,
    )
    return await con.fetch(sql)


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
    assert tree != ""


# -- Tests are sorted in the same order as rules in OFL.g4
#


async def test_expression_and_expression():
    filter = "natural=tree and leaf_type=broadleaved"
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


async def test_expression_or_expression():
    filter = "natural=tree or leaf_type=broadleaved"
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


@pytest.mark.parametrize(
    "filter",
    (
        "not natural=tree",
        "not natural!=tree",
        "not natural=*",
        "not highway in (residential, living_street)",
        "not type:node",
        "not id:node/4540889804",
        "not geometry:point",
        "not area:(1.0..1E6)",
        "not length:(1.0..99.99)",
    ),
)
async def test_not_expression(filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


@pytest.mark.parametrize(
    "filters",
    (
        ("not natural=tree", "natural!=tree"),
        ("natural=tree", "not natural!=tree"),
        ("natural=tree", "not not natural=tree"),
        (
            "not highway in (residential, living_street)",
            "highway=* and highway!=residential and highway!=living_street",
        ),
        ("not type:node", "type:way or type:relation"),
        ("not geometry:point", "geometry:line or geometry:polygon or geometry:other"),
        ("not length:(..99.99)", "length:(99.99..)"),
        ("not length:(..1e6)", "length:(1e6..)"),
    ),
)
async def test_not_expression_comparison(filters):
    sql_where_clause_1 = ohsome_filter_to_sql(filters[0])
    sql_where_clause_2 = ohsome_filter_to_sql(filters[1])
    sql_1 = "SELECT COUNT(*) FROM contributions WHERE " + sql_where_clause_1
    sql_2 = "SELECT COUNT(*) FROM contributions WHERE " + sql_where_clause_2
    results_1: list[Record] = await execute_query(sql_1)
    results_2: list[Record] = await execute_query(sql_2)
    assert results_1 == results_2


@pytest.mark.parametrize(
    "filter",
    (
        "(natural=tree)",
        "((natural=tree))",
        '("addr:housenumber"=45 and "addr:street"="Berliner Straße") or name="HeiGIT"',
        'not ("addr:housenumber"=45 and "addr:street"="Berliner Straße") or name="HeiGIT"',  # noqa
        "(not natural=tree)",
    ),
)
async def test_expression_in_brakets(filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


@pytest.mark.skip("Not implemented yet.")
async def test_hashtag_match():
    filter = "hashtag:missingmaps"
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


@pytest.mark.skip("Not implemented yet.")
@pytest.mark.parametrize(
    "filter",
    (
        "hashtag:(missingmaps)",
        "hashtag:(missingmaps, type, other)",
    ),
)
async def test_hashtag_list_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


# TODO
# add tests for all grammar keywords like number, geometry, id, ...
@pytest.mark.parametrize(
    "filter",
    (
        "natural=tree",
        "natural = tree",
        "natural= tree",
        "natural =tree",
        "natural=Tree",  # case sensitive
        '"addr:housenumber"="45"',
        "type=boundary",  # w/ keyword as key
        "building=other",  # w/ keyword as value
        "addr:housenumber=*",  # key with colon
        '"natüröa"="yes"',  # quoting string should always work and will be escaped
        '"*"="*"',
        "maxspeed=30",
        "oneway!=yes",
        "oneway != yes",
        "oneway!= yes",
        "oneway !=yes",
        (
            '"natural*^what🙈"="🙈ohno != erf = and or" or "natural or *^what🙈" = '
            + '"🙈ohno != erf = and or"'
        ),
        '"na\\"tural*^what🙈"="🙈ohno \\"abc\\\\!= erf = and or"',
        'natural=* and not "natürla"=*',
        "sidewalk::left=yes",
        "sidewalk:=yes",
        "sidewalk : left = yes",  # whitespace between tokens is skipped by the lexer
        '"sidewalk : left" = yes',  # whitespace in quoted string is preserved
    ),
)
async def test_tag_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


@pytest.mark.parametrize(
    "filter",
    (
        "natural=*",
        "name!=*",
        '"*"=*',
        '"*"!=*',
    ),
)
async def test_tag_wildcard_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


@pytest.mark.parametrize(
    "filter",
    (
        "*=*",
        "natürla=*",
    ),
)
async def test_tag_match_invalid(filter):
    with pytest.raises((LexerValueError, ParserValueError)) as e:
        ohsome_filter_to_sql(filter)
    verify(filter + "\n\n" + str(e.value))


@pytest.mark.parametrize(
    "filter",
    (
        "highway in (residential, living_street)",
        "highway in ( residential,living_street )",
        '"type" in (boundary, route)',  #       w/keyword as key
        'highway in (residential, "other")',  # w/keyword quoted as value
        "natural in (water)",  #                w/keyword with single value
    ),
)
async def test_tag_list_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


@pytest.mark.parametrize(
    "filter",
    (
        "cuisine ~ *pizza*",
        "cuisine~*pizza*",
        'name ~ *"straße"',  # quoted
        "maxspeed ~ * mph",  # whitespace is skipped
        'maxspeed ~ *" mph"',  # whitespace is preserved
        "name ~ S*",
        'name ~ "Hotel **"',  # literal * in quoted string
        'name ~ "foo\'bar"',  # potential sql injection vector
        'name ~ "%"',  # literal % needs to be escaped
        "name ~ *_*",  # literal _ needs to be escaped
    ),
)
async def test_tag_value_pattern_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


@pytest.mark.parametrize(
    "filter",
    (
        "key ~ *",
        "key ~ foo*bar",
    ),
)
async def test_tag_value_pattern_match_invalid(filter):
    with pytest.raises((LexerValueError, ParserValueError)) as e:
        ohsome_filter_to_sql(filter)
    verify(filter + "\n\n" + str(e.value))


@pytest.mark.parametrize(
    "filter",
    (
        "type:node",
        "type :node",
        "type: node",
        "type : node",
        "type:way",
        "type:relation",
    ),
)
async def test_type_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


async def test_type_match_invalid():
    filter = "type:foo"
    with pytest.raises((LexerValueError, ParserValueError)) as e:
        ohsome_filter_to_sql(filter)
    verify(filter + "\n\n" + str(e.value))


async def test_id_match():
    filter = "id:4540889804"
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


@pytest.mark.parametrize(
    "filter",
    (
        "id:",
        "id:foo",
        "id:1.0",
    ),
)
async def test_id_match_invalid(filter):
    with pytest.raises((LexerValueError, ParserValueError)) as e:
        ohsome_filter_to_sql(filter)
    verify(filter + "\n\n" + str(e.value))


@pytest.mark.parametrize(
    "filter",
    (
        "id:node/4540889804",
        "id :node/4540889804",
        "id: node/4540889804",
        "id : node/4540889804",
        "id:way/1136431018",
        "id:relation/2070281",
    ),
)
async def test_type_id_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


@pytest.mark.parametrize(
    "filter",
    (
        "id:node/ 4540889804",
        "id:node /4540889804",
        "id:node / 4540889804",
    ),
)
async def test_type_id_match_invalid(filter):
    with pytest.raises((LexerValueError, ParserValueError)) as e:
        ohsome_filter_to_sql(filter)
    verify(filter + "\n\n" + str(e.value))


@pytest.mark.parametrize(
    "filter",
    (
        "id:(1..9999)",
        "id :(1..9999)",
        "id: (1..9999)",
        "id : (1..9999)",
        "id:(..9999)",
        "id:(1..)",
        "id:(1..9999) or id:4540889804",
        "id:(1.. 9999)",
        "id:(1 ..9999)",
        "id:(1 .. 9999)",
        "id:( .. 9999)",
        "id:(1 ..)",
    ),
)
async def test_id_range_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


@pytest.mark.parametrize(
    "filter",
    ("id:(1..",),
)
async def test_id_range_match_invalid(filter):
    with pytest.raises(ValueError) as e:
        ohsome_filter_to_sql(filter)
    verify(filter + "\n\n" + str(e.value))


@pytest.mark.parametrize(
    "filter",
    (
        "id:(4540889804)",
        "id: (4540889804)",
        "id :(4540889804)",
        "id : (4540889804)",
        "id:(1136431018, 4540889804, 2070281)",
        "id:( 1136431018,4540889804,2070281 )",
    ),
)
async def test_id_list_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


@pytest.mark.parametrize(
    "filter",
    (
        "id:(1 ..2",
        "id:(1, 2",
        "id:(1, 2,)",
        "id:()",
        "id:(, )",
    ),
)
async def test_id_list_match_invalid(filter):
    with pytest.raises(ValueError) as e:
        ohsome_filter_to_sql(filter)
    verify(filter + "\n\n" + str(e.value))


@pytest.mark.parametrize(
    "filter",
    (
        "id:(node/4540889804)",
        "id :(node/4540889804)",
        "id: (node/4540889804)",
        "id : (node/4540889804)",
        "id:(node/4540889804, way/1136431018, relation/2070281)",
        "id:( node/4540889804,way/1136431018,relation/2070281 )",
        "id:(node/4540889804, relation/2070281) or id:way/1136431018",
    ),
)
async def test_type_id_list_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


@pytest.mark.parametrize(
    "filter",
    (
        "id:(node/4540889804, way/1136431018",
        "id:(node/4540889804, way/1136431018, )",
    ),
)
async def test_type_id_list_match_invalid(filter):
    with pytest.raises(ValueError) as e:
        ohsome_filter_to_sql(filter)
    verify(filter + "\n\n" + str(e.value))


@pytest.mark.parametrize(
    "filter",
    (
        "geometry:point",
        "geometry :point",
        "geometry: point",
        "geometry : point",
        "geometry:line",
        "geometry:polygon",
        "geometry:other",
    ),
)
async def test_geometry_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


@pytest.mark.skip("Not implemented yet.")
async def test_geometry_match_other(filter):
    filter = "geometry:other"
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


@pytest.mark.parametrize(
    "filter",
    (
        "geometry:",
        "geometry:foo",
        "geometry:1",
    ),
)
async def test_gemoetry_match_invalid(filter):
    with pytest.raises(ValueError) as e:
        ohsome_filter_to_sql(filter)
    verify(filter + "\n\n" + str(e.value))


@pytest.mark.parametrize(
    "filter",
    (
        "area:(1.0..1E6)",
        "area :(1.0..1E6)",
        "area: (1.0..1E6)",
        "area : (1.0..1E6)",
        "area:( 1.0..1E6 )",
        "area:(1.3..)",
        "area:(1e6..)",
        "area:(1..1e6)",
        "area:(1.0..1E6) or area:(..0.5)",
        "area:(1..)",
        "area:(..9999)",
        "area:(1..9999)",
        "area:(1.0.. 9999.0)",
        "area:(1.0 ..9999.0)",
        "area:(1.0 .. 9999.0)",
        "area:( .. 9999.0)",
        "area:(1.0 ..)",
    ),
)
async def test_area_range_match(filter):
    # TODO: ValueError: not enough values to unpack (expected 2, got 1)
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


@pytest.mark.parametrize(
    "filter",
    (
        "area:(-1.0..)",
        "area:(1.0..-200)",
        "area:(..-200)",
        "area:(200..1)",
    ),
)
async def test_area_range_invalid(filter):
    with pytest.raises(ValueError) as e:
        ohsome_filter_to_sql(filter)
    verify(filter + "\n\n" + str(e.value))


@pytest.mark.parametrize(
    "filter",
    (
        "length:(1.0..99.99)",
        "length :(1.0..99.99)",
        "length: (1.0..99.99)",
        "length : (1.0..99.99)",
        "length:( 1.0..99.99 )",
        "length:(1E6..)",
        "length:(1e6..)",
        "length:(1.0..99.99) or length:(..0.5)",
        "length:(1..)",
        "length:(1..99)",
        "length:(..99)",
        "length:(1.0.. 10.0)",
        "length:(1.0 ..10.0)",
        "length:(1.0 .. 10.0)",
        "length:( .. 10.0)",
        "length:(1.0 ..)",
        "length:(10.0 .. 100.0)",
    ),
)
async def test_length_range_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


@pytest.mark.parametrize(
    "filter",
    (
        "length:(-1..)",
        "length:(3.0..-200.0)",
        "length:(..-200.0)",
        "length:(200..1)",
    ),
)
async def test_length_range_invalid(filter):
    with pytest.raises(ValueError) as e:
        ohsome_filter_to_sql(filter)
    verify(filter + "\n\n" + str(e.value))


@pytest.mark.skip("Not implemented yet.")
async def test_changeset_match():
    filter = "changeset:1"
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


@pytest.mark.skip("Not implemented yet.")
@pytest.mark.parametrize(
    "filter",
    (
        "changeset:1",
        "changeset :1",
        "changeset: 1",
        "changeset : 1",
        "changeset:(1)",
        "changeset:(1, 300, 4264)",
        "changeset:( 1,300,4264 )",
    ),
)
async def test_changeset_list_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


@pytest.mark.skip("Not implemented yet.")
@pytest.mark.parametrize(
    "filter",
    (
        "changeset:(1..999)",
        "changeset :(1..999)",
        "changeset: (1..999)",
        "changeset : (1..999)",
        "changeset:( 1..999 )",
        "changeset:(1..)",
        "changeset:(..999)",
        "changeset:(50..999) or changeset:(..10)",
    ),
)
async def test_changeset_range_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


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
async def test_changeset_created_by_match(filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


@pytest.mark.parametrize(
    "filter",
    (
        "(landuse=forest or natural=wood) and geometry:polygon",
        "leisure=park and geometry:polygon or amenity=bench and (geometry:point or geometry:line)",  # noqa
        "building=* and building!=no and geometry:polygon",
        (
            "type:way and (highway in (motorway, motorway_link, trunk, trunk_link, "
            + "primary, primary_link, secondary, secondary_link, tertiary, "
            + "tertiary_link, unclassified, residential, living_street, pedestrian) "
            + "or (highway=service and service=alley))"
        ),
        "type:way and highway=residential and name!=* and noname!=yes",
        "geometry:polygon and building=* and building!=no and area:(1E6..)",
    ),
)
async def test_ohsome_api_examples(filter):
    # https://docs.ohsome.org/ohsome-api/v1/filter.html#examples
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


@pytest.mark.parametrize(
    "filter",
    (
        "geometry:line and  (highway=* or railway=platform) and not "
        + '(cycleway=separate or "cycleway:both"=separate or '
        + '("cycleway:right"=separate and "cycleway:left"=separate) or '
        + "indoor=yes or indoor=corridor)",
        "(((highway=footway) or (highway=path and (foot=designated or foot=yes)) or "
        + "(highway=pedestrian) or (highway=steps) or (highway=cycleway and foot=yes) "
        + "or (sidewalk=* and highway!=motorway) or (foot=yes)) and geometry:line)",
    ),
)
async def test_climate_action_navigator_examples(filter):
    sql = ohsome_filter_to_sql(filter)
    assert await validate_and_verify(sql, filter)


# fmt: off
@pytest.mark.parametrize(
    "str, out",
    [
        ("foo", "foo"),
        ("\"foo\"", "foo"),  # noqa: Q003
        ("\"foo bar\"", "foo bar"),  # noqa: Q003
        ("\"foo\\\"bar\"", "foo\"bar"), # noqa: Q003
        ("\"foo\\\\bar\"", "foo\\bar"), # noqa: Q003
        ("\"foo\\\r\nbar\"", "foo\r\nbar"), # noqa: Q003
    ],
)
async def test_strings(str, out):
    assert unescape(str) == out
# fmt: on


async def test_sql_injection():
    # TODO: add example which injects even though json.dumps is used.
    filter = "\"natural';drop table contributions;SELECT 'test\"=*"
    sql = ohsome_filter_to_sql(filter)
    sql = "SELECT COUNT(*) FROM contributions WHERE " + sql
    verify(sql)
    assert await validate_and_verify(sql, filter)
