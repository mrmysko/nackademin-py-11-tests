import pytest
from treecoords import treecoords


def test_base_case():
    # Black formats this super annoyingly.
    # Standard dict with a nested dict.
    assert treecoords({"a": {"b": 1}, "c": 2}) == (
        (
            (
                "a",
                "b",
            ),
            1,
        ),
        (
            ("c",),
            2,
        ),
    )


def test_list_in_dict():
    assert treecoords({"a": ["b", "c"]}) == ((("a",), ["b", "c"]),)


def test_no_dict():
    assert treecoords(["a", "b", 2])
