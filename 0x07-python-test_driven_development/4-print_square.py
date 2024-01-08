#!/usr/bin/python3
def print_square(size):
    """Prints a square with character #

    Args:
        size: The length of the square
        size: Must be an integer

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0

    Returns:
        A square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
