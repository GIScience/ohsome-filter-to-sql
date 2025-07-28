import pytest
from pytest_approval import verify

from ohsome_filter_to_sql.main import build_tree, main


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
    ("natural=tree",),
)
def test_main(filter):
    assert verify(main(filter))
