#!/usr/bin/python3
def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a: The first integer.
        b: The second integer (default is 98).

    Raises:
        TypeError: If either a or b is not an integer or a float.

    Returns:
        The sum of a and b as an integer.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float")

    a = int(a)
    b = int(b)

    return a + b
