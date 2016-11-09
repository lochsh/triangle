import itertools
import random

from hypothesis import given
from hypothesis import strategies as st
import pytest

import triangle


def at_least_one_zero(lst):
    """If a list has no zero elements, make one of them zero"""
    if not any(item == 0 for item in lst):
        lst[random.randint(0, len(lst) - 1)] = 0
    return lst


def at_least_one_neg(lst):
    """If a list has no negative elements, make one of them negative"""
    if not any(item < 0 for item in lst):
        lst[random.randint(0, len(lst) - 1)] *= -1
    return lst


@given(st.lists(st.floats(), max_size=3, min_size=3).map(at_least_one_neg))
def test_if_negative_lengths_return_false(lengths):
    """If one or more of the three lengths are negative, can't be a triangle"""
    assert triangle.is_triangle(*lengths) is False


@given(st.lists(st.floats(), max_size=3, min_size=3).map(at_least_one_zero))
def test_if_any_zero_lengths_return_false(lengths):
    """If one or more of the three lengths are zero, can't be a triangle"""
    assert triangle.is_triangle(*lengths) is False


@given(st.lists(st.floats(), max_size=3, min_size=3))
def test_triangle_inequality(lengths):
    """
    The lengths of a triangle's sides  must satisfy the triangle inequality.

    The length of a side of a triangle is both:
        * less than the sum of the lengths of the other two sides
        * greater than the difference of the lengths of the other two sides
    """
    i = itertools.cycle([0, 1, 2])
    j = itertools.cycle([1, 2, 0])
    k = itertools.cycle([2, 0, 1])

    def inequality_holds():
        for _ in range(3):
            a, b, c = lengths[next(i)], lengths[next(j)], lengths[next(k)]
            yield True if a < (b + c) and a > abs(b - c) else False

    assert all(inequality_holds()) == triangle.triangle_inequality(lengths)


@given(st.lists(st.one_of(st.booleans(), st.none(), st.text()), 3, 3))
def test_bad_type_input(lst):
    with pytest.raises(TypeError):
        triangle.is_triangle(*lst)


# Sanity check example-based tests
def test_345():
    assert triangle.is_triangle(3, 4, 5)


def test_all_zeros():
    assert triangle.is_triangle(0, 0, 0) is False


def test_negative_example():
    assert triangle.is_triangle(-5, 0.9, 100) is False


def test_equilateral():
    assert triangle.is_triangle(1, 1, 1)
