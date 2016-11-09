import itertools


def is_triangle(a, b, c):
    """Given three line lengths, can these lines form a valid triangle?"""
    positive = not any(item <= 0 for item in [a, b, c])
    inequality = triangle_inequality([a, b, c])
    return positive and inequality


def triangle_inequality(lst):
    i = itertools.cycle([0, 1, 2])
    j = itertools.cycle([1, 2, 0])
    k = itertools.cycle([2, 0, 1])

    def inequality_holds():
        for _ in range(3):
            a, b, c = lst[next(i)], lst[next(j)], lst[next(k)]
            yield True if a < (b + c) and a > (b - c) else False

    return all(inequality_holds())
