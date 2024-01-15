#!/usr/bin/python3
'''Module for Rectangle unit tests.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)
        self.assertEqual(rectangle.id, 1)

        with self.assertRaises(TypeError):
            Rectangle("not_an_integer", 10, 2, 3)

        with self.assertRaises(ValueError):
            Rectangle(0, 10, 2, 3)

        with self.assertRaises(ValueError):
            Rectangle(5, -1, 2, 3)

    def test_str_representation(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 2/3 - 5/10")

    def test_area_method(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rectangle.area(), 50)

    def test_display_method(self):
        rectangle = Rectangle(3, 2, 1, 1, 1)
        with self.assertLogs() as logs:
            rectangle.display()

        self.assertEqual(logs.output, ['   ###', '   ###'])

    def test_update_method(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        rectangle.update(2, 8, 4, 5, 6)
        self.assertEqual(str(rectangle), "[Rectangle] (2) 5/10 - 8/4")

        rectangle.update(width=15, y=8)
        self.assertEqual(str(rectangle), "[Rectangle] (2) 5/8 - 15/10")

    def test_to_dictionary_method(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        rectangle_dict = rectangle.to_dictionary()
        expected_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        self.assertEqual(rectangle_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
