import itertools


def is_triangle(a, b, c):
    """Given three line lengths, can these lines form a valid triangle?"""
    if any(type(item) not in (float, int) for item in [a, b, c]):
        raise TypeError('Inputs must be real numbers')

    if any(item <= 0 for item in [a, b, c]):
        return False
    return triangle_inequality([a, b, c])


def triangle_inequality(lengths):
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

    return all(inequality_holds())
