"""Linked lists."""

from __future__ import annotations
from http.client import FOUND
from typing import TypeVar, Generic, Optional
from dataclasses import dataclass

T = TypeVar('T')


@dataclass
class L(Generic[T]):
    """
    A single link in a linked list.

    The `head` attribute gives you the value at the head of
    this list while `tail` gives you the rest of the list,
    or None if the rest is the empty list.

    >>> L(1, L(2, L(3, None)))
    L(1, L(2, L(3, None)))
    """

    head: T
    tail: List[T]

    def __repr__(self) -> str:
        """Representation of this object."""
        return f"L({self.head}, {self.tail})"


List = Optional[L[T]]  # A list is an L() constructor or None


# Direct recursive versions ###########################################


def length(x: List[T]) -> int:
    """
    Compute the length of x.

    >>> length(None)
    0
    >>> length(L(1, None))
    1
    >>> length(L(1, L(2, L(3, None))))
    3
    """
    match x:
        case None: return 0
        case L(_, tail): return 1 + length(x.tail)

def add(x: List[int]) -> int:
    """
    Compute the length of x.

    >>> add(None)
    0
    >>> add(L(1, None))
    1
    >>> add(L(1, L(2, L(3, None))))
    6
    """
    match x:
        case None: return 0
        case L(val, tail): return val + add(tail)

def contains(x: List[T], e: T) -> bool:
    """
    Tell us if e is in x.

    >>> contains(L(1, L(2, L(3, None))), 4)
    False
    >>> contains(L(1, L(2, L(3, None))), 2)
    True
    """
    match x:
        case None: return False
        case L(head, _ ) if head == e: return True
        case L(_, tail): return contains(tail, e)

    


def drop(x: List[T], k: int) -> List[T]:
    """
    Remove the first k elements.

    >>> x = L(1, L(2, L(3, L(4, None))))
    >>> drop(x, 0)
    L(1, L(2, L(3, L(4, None))))
    >>> drop(x, 1)
    L(2, L(3, L(4, None)))
    >>> drop(x, 3)
    L(4, None)
    >>> drop(x, 4)
    >>> drop(x, 5)
    """
    match (k, x):
        case (0, x): return x
        case (_, None): return None
        case (k, L(_, tail)): return drop(tail, k-1)

def keep(x: List[T], k: int) -> List[T]:
    """
    Keep only the first k elements.

    >>> x = L(1, L(2, L(3, L(4, None))))
    >>> keep(x, 0)
    >>> # returns None but doesn't print
    >>> keep(x, 1)
    L(1, None)
    >>> keep(x, 3)
    L(1, L(2, L(3, None)))
    """       
    match (k, x):
        case (0, x): return None
        case (_, None): return None
        case (k, L(head, tail)): return L(head, keep(tail, k-1))


def concat(x: List[T], y: List[T]) -> List[T]:
    """
    Concatenate x and y.

    >>> concat(L(1, L(2, None)), L(3, L(4, None)))
    L(1, L(2, L(3, L(4, None))))
    """
    match x:
        case None: return y
        case L(head, tail): return L(head, concat(tail, y))

def append(x: List[T], e: T) -> List[T]:
    """
    Append e to x.

    >>> append(L(1, L(2, None)), 3)
    L(1, L(2, L(3, None)))
    """
    return concat(x, L(e, None))


def rev(x: List[T]) -> List[T]:
    """
    Reverse a list.

    >>> rev(L(1, L(2, L(3, None))))
    L(3, L(2, L(1, None)))
    """
    match x:
        case None: return None
        case L(head, tail): return append(rev(tail), head)

# Tail-recursive versions ###########################################


def length_tr(x: List[T], acc: int = 0) -> int:
    """
    Compute the length of x.

    >>> length_tr(None)
    0
    >>> length_tr(L(1, None))
    1
    >>> length_tr(L(1, L(2, L(3, None))))
    3
    """
    match x:
        case None: return acc
        case L(_, tail): return length_tr(tail, acc + 1)

def add_tr(x: List[int], acc: int = 0) -> int:
    """
    Compute the length of x.

    >>> add_tr(None)
    0
    >>> add_tr(L(1, None))
    1
    >>> add_tr(L(1, L(2, L(3, None))))
    6
    """
    match x:
        case None: return acc
        case L(head, tail): return add_tr(tail, acc + head)

def contains_tr(x: List[T], e: T) -> bool:
    """
    Tell us if e is in x.

    >>> contains_tr(L(1, L(2, L(3, None))), 4)
    False
    >>> contains_tr(L(1, L(2, L(3, None))), 2)
    True
    """
    return contains(x, e)


def drop_tr(x: List[T], k: int) -> List[T]:
    """
    Remove the first k elements.

    >>> x = L(1, L(2, L(3, L(4, None))))
    >>> drop_tr(x, 0)
    L(1, L(2, L(3, L(4, None))))
    >>> drop_tr(x, 1)
    L(2, L(3, L(4, None)))
    >>> drop_tr(x, 3)
    L(4, None)
    """
    return drop(x, k)


def keep_tr(x: List[T], k: int) -> List[T]:
    """
    Keep only the first k elements.

    >>> x = L(1, L(2, L(3, L(4, None))))
    >>> keep_tr(x, 0) # returns None but doesn't print
    >>> keep_tr(x, 1)
    L(1, None)
    >>> keep_tr(x, 3)
    L(1, L(2, L(3, None)))
    """
    def innner_keep_tr(x, k, acc = None):
        match (k, x):
            case(0, _): return rev(acc)
            case (_, None): return rev(acc)
            case(k, L(head, tail)): return innner_keep_tr(tail, k-1, L(head, acc))
    return innner_keep_tr(x, k)
    


def concat_tr(x: List[T], y: List[T]) -> List[T]:
    """
    Concatenate x and y.

    >>> concat_tr(L(1, L(2, None)), L(3, L(4, None)))
    L(1, L(2, L(3, L(4, None))))
    """
    ...


def append_tr(x: List[T], e: T) -> List[T]:
    """
    Append e to x.

    >>> append_tr(L(1, L(2, None)), 3)
    L(1, L(2, L(3, None)))
    """
    ...


def rev_tr(x: List[T]) -> List[T]:
    """
    Reverse a list.

    >>> rev_tr(L(1, L(2, L(3, None))))
    L(3, L(2, L(1, None)))
    """
    def inner_rev_tr(x, acc = None):
        match x:
            case None: return acc
            case L(head, tail): return inner_rev_tr(tail, L(head, acc))
    return inner_rev_tr(x)


# Loop versions ###########################################

def length_loop(x: List[T]) -> int:
    """
    Compute the length of x.

    >>> length_loop(None)
    0
    >>> length_loop(L(1, None))
    1
    >>> length_loop(L(1, L(2, L(3, None))))
    3
    """
    acc = 0
    while x:
        acc += 1
        x = x.tail
    return acc


def add_loop(x: List[int]) -> int:
    """
    Compute the length of x.

    >>> add_loop(None)
    0
    >>> add_loop(L(1, None))
    1
    >>> add_loop(L(1, L(2, L(3, None))))
    6
    """
    acc = 0
    while x:
        acc += x.head
        x = x.tail
    return acc


def contains_loop(x: List[T], e: T) -> bool:
    """
    Tell us if e is in x.

    >>> contains_loop(L(1, L(2, L(3, None))), 4)
    False
    >>> contains_loop(L(1, L(2, L(3, None))), 2)
    True
    """
    ...


def drop_loop(x: List[T], k: int) -> List[T]:
    """
    Remove the first k elements.

    >>> x = L(1, L(2, L(3, L(4, None))))
    >>> drop_loop(x, 0)
    L(1, L(2, L(3, L(4, None))))
    >>> drop_loop(x, 1)
    L(2, L(3, L(4, None)))
    >>> drop_loop(x, 3)
    L(4, None)
    """
    ...


def keep_loop(x: List[T], k: int) -> List[T]:
    """
    Keep only the first k elements.

    >>> x = L(1, L(2, L(3, L(4, None))))
    >>> keep_loop(x, 0) # returns None but doesn't print
    >>> keep_loop(x, 1)
    L(1, None)
    >>> keep_loop(x, 3)
    L(1, L(2, L(3, None)))
    """
    ...


def concat_loop(x: List[T], y: List[T]) -> List[T]:
    """
    Concatenate x and y.

    >>> concat_loop(L(1, L(2, None)), L(3, L(4, None)))
    L(1, L(2, L(3, L(4, None))))
    """
    ...


def append_loop(x: List[T], e: T) -> List[T]:
    """
    Append e to x.

    >>> append_loop(L(1, L(2, None)), 3)
    L(1, L(2, L(3, None)))
    """
    ...


def rev_loop(x: List[T]) -> List[T]:
    """
    Reverse a list.

    >>> rev_loop(L(1, L(2, L(3, None))))
    L(3, L(2, L(1, None)))
    """
    ...
