#!/usr/bin/python3
"""unittest for Base class.

    TestBase_Initialization - line 19
    TestBase_ToJsonString - line 117
    TestBase_FromJsonString - line 179
    TestBase_Create - line 241
    TestBase_SaveToFile - 271
    TestBase_LoadFromFile - 318
"""
import os
import json
import unittest
import models
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_Documentation(unittest.TestCase):
    """Unittest for documentation."""

    def test_base_module(self):
        self.assertIsNotNone(models.base.__doc__)
        self.assertNotEqual(models.base.__doc__, "")

    def test_Base_class(self):
        self.assertIsNotNone(Base.__doc__)
        self.assertNotEqual(Base.__doc__, "")

    def test_to_json_string_method(self):
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertNotEqual(Base.to_json_string.__doc__, "")

    def test_from_json_string_method(self):
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertNotEqual(Base.from_json_string.__doc__, "")

    def test_create_method(self):
        self.assertIsNotNone(Base.create.__doc__)
        self.assertNotEqual(Base.create.__doc__, "")

    def test_save_to_file_method(self):
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertNotEqual(Base.save_to_file.__doc__, "")

    def test_load_from_file_method(self):
        self.assertIsNotNone(Base.load_from_file.__doc__)
        self.assertNotEqual(Base.load_from_file.__doc__, "")


class TestBase_Initialization(unittest.TestCase):
    """Unittest for the initialization of the class Base"""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_arg(self):
        b1 = Base(12)
        b2 = Base(24)
        self.assertEqual(b1.id, 12)
        self.assertEqual(b2.id, 24)

    def test_no_arg_and_arg(self):
        b1 = Base()
        b2 = Base(18)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_None_arg(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_setter(self):
        b = Base(36)
        self.assertEqual(b.id, 36)
        b.id = 48
        self.assertEqual(b.id, 48)

    def test_private__nb_objects(self):
        with self.assertRaises(AttributeError):
            Base.__nb_objects

    def test_float_arg(self):
        b1 = Base(2.7)
        b2 = Base(float(3))
        self.assertEqual(b1.id, 2.7)
        self.assertEqual(b2.id, float(3))

    def test_complex_arg(self):
        b = Base(2 + 4j)
        self.assertEqual(b.id, 2 + 4j)

    def test_string_arg(self):
        b = Base(str(id))
        self.assertEqual(b.id, str(id))

    def test_tuple_arg(self):
        b = Base((1, 2, 3))
        self.assertEqual(b.id, (1, 2, 3))

    def test_list_arg(self):
        b = Base([3, 4, 5])
        self.assertEqual(b.id, [3, 4, 5])

    def test_range_arg(self):
        b = Base(range(10))
        self.assertEqual(b.id, range(10))

    def test_dictionary_arg(self):
        b = Base({"a": 1, "b": 2})
        self.assertEqual(b.id, {"a": 1, "b": 2})

    def test_bool_arg(self):
        b1 = Base(True)
        b2 = Base(False)
        self.assertEqual(b1.id, True)
        self.assertEqual(b2.id, False)

    def test_set_arg(self):
        b = Base({"a", "set"})
        self.assertEqual(b.id, set(("a", "set")))

    def test_frozenset_arg(self):
        b = Base(frozenset(('a', 'b', 'c')))
        self.assertEqual(b.id, frozenset(('a', 'b', 'c')))

    def test_bytes_arg(self):
        b = Base(b'a byte ???')
        self.assertEqual(b.id, bytes("a byte ???", 'utf-8'))

    def test_memoryview_arg(self):
        b = Base(memoryview(b'I see you'))
        self.assertEqual(b.id, memoryview(b'I see you'))

    def test_nan_arg(self):
        b = Base(float("nan"))
        self.assertEqual(type(b.id), type(float("nan")))

    def test_inf_arg(self):
        b = Base(float("inf"))
        self.assertEqual(b.id, float("inf"))

    def test_multiple_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2, 3)


class TestBase_ToJsonString(unittest.TestCase):
    """Unittests on the to_json_string static method of the Base Class."""

    def test_none_arg(self):
        list_dictionaries = None
        json_string = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_string, "[]")

    def test_empty_dictionary(self):
        list_dictionaries = []
        json_string = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_string, "[]")

    def test_list_of_dictionary(self):
        list_dictionaries = [{"a": 1, "b": 2}]
        json_string = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_string, '[{"a": 1, "b": 2}]')

    def test_list_of_dictionaries(self):
        list_dictionaries = [{"a": 1, "b": 2}, {"c": 3, "d": 4}]
        json_string = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_string, '[{"a": 1, "b": 2}, {"c": 3, "d": 4}]')

    def test_set(self):
        list_dictionaries = {"a", "b"}
        with self.assertRaises(TypeError):
            Base.to_json_string(list_dictionaries)

    def test_dictionary(self):
        list_dictionaries = {"a": 1, "b": 2}
        json_string = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_string, '{"a": 1, "b": 2}')

    def test_int(self):
        list_dictionaries = 6
        json_string = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_string, str(6))

    def test_float(self):
        list_dictionaries = 7.5
        json_string = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_string, str(7.5))

    def test_string(self):
        list_dictionaries = "hello"
        json_string = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_string, str('"hello"'))

    def test_bool(self):
        list_dictionaries = True
        json_string = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_string, "true")
        list_dictionaries = False
        json_string = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_string, "false")

    def test_tuple(self):
        list_dictionaries = (1, 2, 3)
        json_string = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_string, "[1, 2, 3]")


class TestBase_FromJsonString(unittest.TestCase):
    """Unittests on the from_json_string static method of the Base Class."""

    def test_none_arg(self):
        json_string = None
        obj = Base.from_json_string(json_string)
        self.assertEqual(obj, [])

    def test_empty_string(self):
        json_string = ""
        obj = Base.from_json_string(json_string)
        self.assertEqual(obj, [])

    def test_string_empty_list(self):
        json_string = "[]"
        obj = Base.from_json_string(json_string)
        self.assertEqual(obj, [])

    def test_string_list_of_dictionaries(self):
        json_string = '[{"a": 1, "b": 2}, {"c": 3, "d": 4}]'
        obj = Base.from_json_string(json_string)
        self.assertEqual(obj, [{"a": 1, "b": 2}, {"c": 3, "d": 4}])

    def test_string_set(self):
        json_string = '{"a", "b"}'
        with self.assertRaises(json.decoder.JSONDecodeError):
            Base.from_json_string(json_string)

    def test_string_dictionary(self):
        json_string = '{"a": 1, "b": 2}'
        obj = Base.from_json_string(json_string)
        self.assertEqual(obj, {"a": 1, "b": 2})

    def test_string_int(self):
        json_string = '6'
        obj = Base.from_json_string(json_string)
        self.assertEqual(obj, 6)

    def test_string_float(self):
        json_string = '7.5'
        obj = Base.from_json_string(json_string)
        self.assertEqual(obj, 7.5)

    def test_string(self):
        json_string = "hello"
        with self.assertRaises(json.decoder.JSONDecodeError):
            Base.from_json_string(json_string)

    def test_string_bool(self):
        json_string = 'true'
        obj = Base.from_json_string(json_string)
        self.assertEqual(obj, True)
        json_string = 'false'
        obj = Base.from_json_string(json_string)
        self.assertEqual(obj, False)

    def test_string_tuple(self):
        json_string = '(1, 3, 4)'
        with self.assertRaises(json.decoder.JSONDecodeError):
            Base.from_json_string(json_string)


class TestBase_Create(unittest.TestCase):
    """Unittests on the create class method of the Base Class."""

    def test_none(self):
        with self.assertRaises(TypeError):
            Base.create(None)

    def test_empty_dictionary(self):
        dictionary = {}
        b = Base.create(**dictionary)
        self.assertIsNone(b)

    def test_dictionary(self):
        dictionary = {"id": 1}
        with self.assertRaises(AttributeError):
            Base.create(**dictionary)

    def test_int(self):
        with self.assertRaises(TypeError):
            Base.create(20)

    def test_float(self):
        with self.assertRaises(TypeError):
            Base.create(20.5)

    def test_string(self):
        with self.assertRaises(TypeError):
            Base.create("id of 1")

    def test_Rectangle(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_Square(self):
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)


class TestBase_SaveToFile(unittest.TestCase):
    """Unittests on save_to_file class method of the Base Class."""

    def setUp(self):
        self.filenames = ["Base.json", "Rectangle.json", "Square.json"]

    def test_none(self):
        list_objs = None
        Base.save_to_file(list_objs)

        with open(self.filenames[0]) as json_file:
            self.assertEqual(json_file.read(), "[]")

    def test_empty_list(self):
        list_objs = []
        Base.save_to_file(list_objs)

        with open(self.filenames[0]) as json_file:
            self.assertEqual(json_file.read(), "[]")

    def test_list_of_objs(self):
        b1 = Base()
        b2 = Base()
        list_objs = [b1, b2]
        with self.assertRaises(AttributeError):
            Base.save_to_file(list_objs)

    def test_list_of_ints(self):
        list_objs = [1, 2]
        with self.assertRaises(AttributeError):
            Base.save_to_file(list_objs)

    def test_list_of_strings(self):
        list_objs = ["hs", "ht"]
        with self.assertRaises(AttributeError):
            Base.save_to_file(list_objs)

    def test_non_iterable(self):
        obj = 456
        with self.assertRaises(TypeError):
            Base.save_to_file(obj)

    def test_Rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open(self.filenames[1], "r") as json_file:
            list_dicts = Rectangle.from_json_string(json_file.read())
        self.assertEqual(list_dicts, [r1.to_dictionary(), r2.to_dictionary()])

    def test_Square(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        Square.save_to_file([s1, s2])

        with open(self.filenames[2], "r") as json_file:
            list_dicts = Square.from_json_string(json_file.read())
        self.assertEqual(list_dicts, [s1.to_dictionary(), s2.to_dictionary()])

    def tearDown(self):
        for filename in self.filenames:
            if os.path.isfile(filename):
                os.remove(filename)


class TestBase_LoadFromFile(unittest.TestCase):
    """Unittests on load_file class method of the Base Class."""
    def setUp(self):
        self.filenames = ["Base.json", "Rectangle.json", "Square.json"]

    def test_no_file(self):
        self.assertEqual(Base.load_from_file(), [])

    def test_Rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_input = [r1, r2]

        Rectangle.save_to_file(list_input)

        list_output = Rectangle.load_from_file()

        for i in range(2):
            self.assertIsNot(list_input[i], list_output[i])

    def test_Square(self):
        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4)
        list_input = [r1, r2]

        Square.save_to_file(list_input)

        list_output = Square.load_from_file()

        for i in range(2):
            self.assertIsNot(list_input[i], list_output[i])

    def tearDown(self):
        for filename in self.filenames:
            if os.path.isfile(filename):
                os.remove(filename)


if __name__ == '__main__':
    unittest.main()
