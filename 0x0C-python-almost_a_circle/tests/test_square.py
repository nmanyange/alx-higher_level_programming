#!/usr/bin/python3
'''Module for Square unit tests.'''
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_constructor(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

        with self.assertRaises(TypeError):
            Square("not_an_integer")

        with self.assertRaises(ValueError):
            Square(0)

        with self.assertRaises(ValueError):
            Square(-1)

    def test_str_representation(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    def test_size_property(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)

        square.size = 10
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

    def test_update_method(self):
        square = Square(5, 2, 3, 1)
        square.update(2, 10, 4, 5)
        self.assertEqual(str(square), "[Square] (2) 4/5 - 10")

        square.update(size=15, y=8)
        self.assertEqual(str(square), "[Square] (2) 4/8 - 15")

    def test_to_dictionary_method(self):
        square = Square(5, 2, 3, 1)
        square_dict = square.to_dictionary()
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
