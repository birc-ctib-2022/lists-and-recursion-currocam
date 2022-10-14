# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from lists import (
    L, List, append_tr, concat_tr, contains_loop, drop_loop, keep_loop, keep_tr,
    length, add, contains, drop, keep, concat, append, length_tr, rev, rev_tr
)
from typing import TypeVar, Sequence

T = TypeVar('T')

# Helper functions for translating to and from Python lists


def from_python_list(x: Sequence[T]) -> List[T]:
    """Make a linked list from a Python sequence."""
    lst = None
    for a in reversed(x):
        lst = L(a, lst)
    return lst


def to_python_list(x: List[T]) -> list[T]:
    """Make a linked list into a Python list."""
    lst = []
    while x is not None:
        lst.append(x.head)
        x = x.tail
    return lst

# Test functions


def test_list_conversion() -> None:
    """Test if we can go from and to python lists."""
    x = [1, 2, 3]
    assert to_python_list(from_python_list(x)) == x


def test_length() -> None:
    """Test that the length function works."""
    for i in range(10):
        lst = from_python_list(list(range(i)))
        assert length(lst) == i
        assert length_tr(lst) == i


def test_add() -> None:
    """Test that the add function works."""
    for i in range(10):
        x = list(range(i))
        y = from_python_list(x)
        assert sum(x) == add(y)


def test_contains() -> None:
    """Test that the contains function works."""
    x = list(range(5, 8))
    y = from_python_list(x)
    for i in range(10):
        assert (i in x) == contains(y, i)


def test_drop() -> None:
    """Test that the drop function works."""
    x = list(range(10))
    y = from_python_list(x)
    for i in range(10):
        assert x[i:] == to_python_list(drop(y, i))


def test_keep() -> None:
    """Test that the keep function works."""
    x = list(range(10))
    y = from_python_list(x)
    for i in range(10):
        assert x[:i] == to_python_list(keep(y, i))
        assert x[:i] == to_python_list(keep_tr(y, i))


def test_concat() -> None:
    """Test that the concat function works."""
    for i in range(10):
        x = list(range(i))
        y = from_python_list(x)
        assert to_python_list(concat(y, y)) == x + x
        assert to_python_list(concat_tr(y, y)) == x + x


def test_append() -> None:
    """Test that the append function works."""
    x = []
    y = None
    for i in range(10):
        x.append(i)
        y = append(y, i)
        assert to_python_list(y) == x


def test_rev() -> None:
    """Test that the rev function works."""
    x = []
    y = None
    for i in range(10):
        x.append(i)
        y = append(y, i)
        assert to_python_list(rev(y)) == x[::-1]
        assert to_python_list(rev_tr(y)) == x[::-1]


def test_contains_loop():
    """Test that loop version of contains works"""
    x = list(range(1,  1500, 1))
    y = from_python_list(x)
    for i in range(1000, 1100, 10):
        assert (i in x) == contains_loop(y, i)

def test_drop() -> None:
    """Test that the drop loop function works."""
    x = list(range(1,  1500, 1))
    y = from_python_list(x)
    for i in range(1000, 1200, 10):
        assert x[i:] == to_python_list(drop_loop(y, i))

def test_keep_loop() -> None:
    """Test that the keep loop function works."""
    x = list(range(2000))
    y = from_python_list(x)
    for i in range(1000, 1100, 10):
        assert x[:i] == to_python_list(keep_loop(y, i))