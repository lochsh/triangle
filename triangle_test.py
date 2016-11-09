from hypothesis import given
from hypothesis import strategies as st
import random

import triangle


def at_least_one_zero(lst):
    if not any(item == 0 for item in lst):
        lst[random.randint(0, len(lst) - 1)] = 0
    return lst


@given(st.integers())
@given(st.integers())
@given(st.integers(max_value=-1))
def test_if_negative_length_return_false(a, b, c):
    """If one or more of the three lengths are negative, can't be a triangle"""
    assert triangle.is_triangle(a, b, c) is False


@given(st.lists(st.integers(), max_size=3, min_size=3).map(at_least_one_zero))
def test_if_any_zeros_length_return_false(lst):
    """If one or more of the three lengths are zero, can't be a triangle"""
    assert triangle.is_triangle(*lst) is False
