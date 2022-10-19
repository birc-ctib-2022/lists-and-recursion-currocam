# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

import sys

from lists import (
    L, List, add_loop, add_tr, append_loop, append_tr, concat_loop, concat_tr, contains_loop, contains_tr, drop_loop, drop_tr, keep_loop, keep_tr,
    length, add, contains, drop, keep, concat, append, length_loop, length_tr, rev, rev_loop, rev_tr
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

def _test_variants(inner, f1, f2, f3) -> None:
    sys.setrecursionlimit(1000)
    inner(f1)
    inner(f2)
    sys.setrecursionlimit(50)
    inner(f3)

def test_length() -> None:
    """Test that the length function works."""
    def inner(fn):
        for i in range(50):
            lst = from_python_list(list(range(i)))
            assert fn(lst) == i
    _test_variants(inner, length, length_tr, length_loop)


def test_add() -> None:
    """Test that the add function works."""
    def inner(fn):
        for i in range(10):
            x = list(range(i))
            y = from_python_list(x)
            assert sum(x) == fn(y)
    _test_variants(inner, add, add_tr, add_loop)




def test_contains() -> None:
    """Test that the contains function works."""
    def inner(fn):
        x = list(range(5, 35))
        y = from_python_list(x)
        for i in range(10):
            assert (i in x) == fn(y, i)
    _test_variants(inner, contains, contains_tr, contains_loop)


def test_keep() -> None:
    """Test that the keep function works."""
    def inner(fn):
        x = list(range(10))
        y = from_python_list(x)
        for i in range(10):
            assert x[:i] == to_python_list(fn(y, i))
    _test_variants(inner, keep, keep_tr, keep_loop)

def test_drop_works() -> None:
    """Test that the drop function works."""
    def inner(fn):
        x = list(range(100))
        y = from_python_list(x)
        for i in range(100):
            assert x[i:] == to_python_list(fn(y, i))
    _test_variants(inner, drop, drop_tr, drop_loop)

def test_concat() -> None:
    """Test that the concat function works."""
    def inner(fn):
        for i in range(100):
            x = list(range(i))
            y = from_python_list(x)
            assert to_python_list(fn(y, y)) == x + x
    _test_variants(inner, concat, concat_tr, concat_loop)


def test_append() -> None:
    """Test that the append function works."""
    def inner(fn):
        x = []
        y = None
        for i in range(10):
            x.append(i)
            y = fn(y, i)
            assert to_python_list(y) == x
    _test_variants(inner, append, append_tr, append_loop)


def test_rev() -> None:
    """Test that the rev function works."""
    def inner(fn):
        x = []
        y = None
        for i in range(10):
            x.append(i)
            y = append(y, i)
            assert to_python_list(fn(y)) == x[::-1]
    _test_variants(inner, rev, rev_tr, rev_loop)
