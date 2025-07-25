import pytest
from pytest_approval import verify

from ohsome_filter_to_sql.main import build_tree


@pytest.mark.parametrize(
    "filter",
    (
        "natural=tree",
        "type:node and natural=tree",
        "id:(node/1, way/2) and type:way",
    ),
)
def test_tag(filter):
    tree = build_tree(filter).toStringTree()
    assert verify(tree)
