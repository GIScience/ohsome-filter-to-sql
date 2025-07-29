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
        "natural=tree",  #             tagMatch
        '"type"=boundary',  #          tagMatch w/ keyword as key
        'name="other"',  #             tagMatch w/ keyword as value
        "natural=*",  #                tagWildcardMatch
        "natural!=tree",  #            tagNotMatch
        "natural!=*",  #               tagNotWildcardMatch
        # "natural in (tree, water)",  # tagListMatch  # TODO
    ),
)
def test_main(filter):
    query = main(filter)
    assert verify(query)
    validate("SELECT * FROM foo WHERE " + query)
