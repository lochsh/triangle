def is_triangle(a, b, c):
    return not any(item <= 0 for item in [a, b, c])
