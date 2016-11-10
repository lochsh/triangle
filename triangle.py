def is_triangle(a, b, c):
    """
    Given three line lengths, can these lines form a valid triangle?

    The lengths of a triangle's sides  must satisfy the triangle inequality,
    meaning the length of a side of a triangle is both:
        * less than the sum of the lengths of the other two sides
        * greater than the difference of the lengths of the other two sides

    This can be reduced to 2 * (longest length) < (sum of lengths)
    """
    lengths = [a, b, c]

    if any(type(item) not in (float, int) for item in lengths):
        raise TypeError('Inputs must be real numbers')

    return 2 * max(lengths) < sum(lengths)
