def is_triangle(a, b, c):
    """
    Given three line lengths, can these lines form a valid triangle?

    Each of the lengths of a triangle's sides must be less than the sum of the
    lengths of the other two sides.  We can reduce this to the following for
    lengths a, b, c: b + c > a > abs(b - c)
    """
    return True if a < (b + c) and a > abs(b - c) else False
