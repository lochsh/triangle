import math
import random

from hypothesis import given
from hypothesis import strategies as st
import pytest

import triangle

length_3 = {'max_size': 3, 'min_size': 3}


def at_least_one_zero(lst):
    """If a list has no zero elements, make one of them zero"""
    if not any(item == 0 for item in lst):
        lst[random.randint(0, len(lst) - 1)] = 0
    return lst


def at_least_one_negative(lst):
    """If a list has no negative elements, make one of them negative"""
    if not any(item < 0 for item in lst):
        lst[random.randint(0, len(lst) - 1)] *= -1
    return lst


@given(st.lists(st.floats(), **length_3).map(at_least_one_negative))
def test_negative_lengths_return_false(lengths):
    assert triangle.is_triangle(*lengths) is False


@given(st.lists(st.floats(), **length_3).map(at_least_one_zero))
def test_zero_lengths_return_false(lengths):
    assert triangle.is_triangle(*lengths) is False


@given(st.integers(9, 10e6).map(lambda x: (x - 1 + int(x % 2))))
def test_pythagorean_triples(a_sq):
    b_sq = ((a_sq - 1)/2)**2
    c_sq = b_sq + a_sq
    assert triangle.is_triangle(*[math.sqrt(i) for i in [a_sq, b_sq, c_sq]])


def machine_precision_insurance(lengths):
    a, _, c = sorted(lengths)
    if abs(math.log10(c / a)) > 7:
        lengths[lengths.index(c)] *= a
    return lengths


@given(st.lists(st.floats(min_value=0.1, max_value=1e100),
                **length_3).map(machine_precision_insurance))
def test_lengths_from_valid_angles(lengths):

    def angles():
        a, b, c = lengths
        for _ in range(3):
            yield math.acos((a**2 + b**2 - c**2) / (2*a*b))
            a, b, c = b, c, a

    def valid_angles():
        try:
            positive = True if not any(i <= 0 for i in angles()) else False
            sum_to_pi = math.isclose(sum(angles()), math.pi, rel_tol=1e-7)
            return positive and sum_to_pi
        except (ValueError, OverflowError):
            return False

    assert triangle.is_triangle(*lengths) == valid_angles()


def test_machine_precision_large():
    assert triangle.is_triangle(1e100, 0.1, 1e100)


def test_machine_precision_small():
    assert triangle.is_triangle(1e-100, 1e-150, 1e-100)


@given(st.lists(st.one_of(st.none(), st.complex_numbers()), **length_3))
def test_bad_type_input(lst):
    with pytest.raises(TypeError):
        triangle.is_triangle(*lst)


def test_345():
    assert triangle.is_triangle(3, 4, 5)


def test_all_zeros():
    assert triangle.is_triangle(0, 0, 0) is False


def test_negative_example():
    assert triangle.is_triangle(-5, 0.9, 100) is False


def test_equilateral():
    assert triangle.is_triangle(1, 1, 1)
