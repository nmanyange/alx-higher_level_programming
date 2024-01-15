#!/usr/bin/python3
'''Module for Base unit tests.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_constructor_with_id(self):
        base_with_id = Base(10)
        self.assertEqual(base_with_id.id, 10)

    def test_constructor_without_id(self):
        base_without_id_1 = Base()
        base_without_id_2 = Base()
        self.assertEqual(base_without_id_1.id, 1)
        self.assertEqual(base_without_id_2.id, 2)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")
        input_list = [{'key': 'value'}, {'key2': 'value2'}]
        expected_output = '[{"key": "value"}, {"key2": "value2"}]'
        self.assertEqual(Base.to_json_string(input_list), expected_output)

    def test_save_to_file(self):
        # Assuming save_to_file method is tested along with create and to_json_string methods
        # Mocking the file write operation for testing

        # Write a test JSON file
        test_filename = "Base_test.json"
        test_json_data = '[{"id": 1, "name": "TestObject"}]'
        with open(test_filename, 'w') as test_file:
            test_file.write(test_json_data)

        # Load the data from the test file
        instances = Base.load_from_file(test_filename)
        self.assertEqual(len(instances), 1)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[0].name, "TestObject")

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string(None), [])
        input_string = '[{"key": "value"}, {"key2": "value2"}]'
        expected_output = [{'key': 'value'}, {'key2': 'value2'}]
        self.assertEqual(Base.from_json_string(input_string), expected_output)

    def test_create_method(self):
        rectangle_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        square_dict = {'id': 2, 'size': 5, 'x': 1, 'y': 2}

        rectangle_instance = Base.create(**rectangle_dict)
        square_instance = Base.create(**square_dict)

        self.assertEqual(rectangle_instance.id, 1)
        self.assertEqual(rectangle_instance.width, 5)
        self.assertEqual(rectangle_instance.height, 10)

        self.assertEqual(square_instance.id, 2)
        self.assertEqual(square_instance.size, 5)

    def test_load_from_file_method(self):
        # Assuming load_from_file method is tested along with create and from_json_string methods
        # Mocking the file read operation for testing

        # Write a test JSON file
        test_filename = "Base_test.json"
        test_json_data = '[{"id": 1, "name": "TestObject"}]'
        with open(test_filename, 'w') as test_file:
            test_file.write(test_json_data)

        # Load the data from the test file
        instances = Base.load_from_file(test_filename)
        self.assertEqual(len(instances), 1)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[0].name, "TestObject")


if __name__ == '__main__':
    unittest.main()
