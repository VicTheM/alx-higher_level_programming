#!/usr/bin/python3
"""unittest for Square class.

    TestSquare_Initialization - line 18
    TestSquare_Size - line 139
    TestSquare_Update - line 231
    TestSquare_ToDictionary - line 300
    TestSquare___Str__  - line 365
"""
import models
import unittest
import unittest.mock
from io import StringIO
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestSquare_Documentation(unittest.TestCase):
    """Unittest for the documentation."""

    def test_Square_module(self):
        self.assertIsNotNone(models.square.__doc__)
        self.assertNotEqual(models.square.__doc__, "")

    def test_Sqaure_class(self):
        self.assertIsNotNone(Square.__doc__)
        self.assertNotEqual(Square.__doc__, "")

    def test_update_method(self):
        self.assertIsNotNone(Square.update.__doc__)
        self.assertNotEqual(Square.update.__doc__, "")

    def test_to_dictionary_method(self):
        self.assertIsNotNone(Square.to_dictionary.__doc__)
        self.assertNotEqual(Square.to_dictionary.__doc__, "")

    def test___str___method(self):
        self.assertIsNotNone(Square.__str__.__doc__)
        self.assertNotEqual(Square.__str__.__doc__, "")


class TestSquare_Initialization(unittest.TestCase):
    """Unittest for the initialization of the class Square."""

    def test_isinstance_Base(self):
        self.assertIsInstance(Square(1), Base)

    def test_isinstance_Rectangle(self):
        self.assertIsInstance(Square(1), Rectangle)

    def test_zero_arg(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(1)
        s2 = Square(1)
        self.assertEqual(s1.id, s2.id - 1)
        self.assertIsNot(s1, s2)

    def test_two_args(self):
        s1 = Square(1, 2)
        s2 = Square(1, 2)
        self.assertEqual(s1.id, s2.id - 1)
        self.assertIsNot(s1, s2)

    def test_three_arg3(self):
        s1 = Square(1, 2, 3)
        s2 = Square(1, 2, 3)
        self.assertEqual(s1.id, s2.id - 1)
        self.assertIsNot(s1, s2)

    def test_four_args(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(1, 2, 3, 4)
        self.assertEqual(s1.id, s2.id)
        self.assertIsNot(s1, s2)

    def test_more_than_four_args(self):
        with self.subTest("5"):
            with self.assertRaises(TypeError):
                Square(1, 2, 3, 4, 5)
        with self.subTest("6"):
            with self.assertRaises(TypeError):
                Square(1, 2, 3, 4, 5, 6)

    def test_size_getter(self):
        s = Square(10)
        self.assertEqual(s.size, 10)

    def test_size_setter(self):
        s = Square(10)
        s.size = 50
        self.assertEqual(s.size, 50)

    def test_width_getter(self):
        s = Square(6)
        self.assertEqual(s.width, 6)

    def test_width_setter(self):
        s = Square(6)
        s.size = 24
        self.assertEqual(s.width, 24)

    def test_height_getter(self):
        s = Square(5)
        self.assertEqual(s.height, 5)

    def test_height_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.height, 10)

    def test_x_getter(self):
        s = Square(3, 7)
        self.assertEqual(s.x, 7)

    def test_x_setter(self):
        s = Square(3, 1, 7)
        s.x = 21
        self.assertEqual(s.x, 21)

    def test_y_getter(self):
        s = Square(2, 3)
        self.assertEqual(s.y, 0)

    def test_y_getter(self):
        s = Square(2, 3, 1)
        s.y = 6
        self.assertEqual(s.y, 6)

    def test_id(self):
        s = Square(1, 3, 4)
        s.id = 104
        self.assertEqual(s.id, 104)

    def test_private_width(self):
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.__size

    def test_private_width(self):
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.__width

    def test_private_height(self):
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.__height

    def test_private_x(self):
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.__x

    def test_private_x(self):
        s = Square(1)
        with self.assertRaises(AttributeError):
            s.__y


class TestSquare_Size(unittest.TestCase):
    """Unittest for the size attribute of the class Square."""

    def setUp(self):
        self.s = Square(1)
        self.err = "width must be an integer"
        self.err1 = "width must be > 0"

    def test_int_size(self):
        self.s.size = 2

    def test_negative_int_size(self):
        with self.assertRaises(ValueError) as err:
            self.s.size = -3
        self.assertEqual(self.err1, str(err.exception))

    def test_zero_size(self):
        with self.assertRaises(ValueError) as err:
            self.s.size = 0
        self.assertEqual(self.err1, str(err.exception))

    def test_float_size(self):
        with self.assertRaises(TypeError) as err:
            self.s.size = 2.5
        self.assertEqual(self.err, str(err.exception))

    def test_complex_size(self):
        with self.assertRaises(TypeError) as err:
            self.s.size = 2 + 7j
        self.assertEqual(self.err, str(err.exception))

    def test_string_size(self):
        with self.assertRaises(TypeError) as err:
            self.s.size = "2"
        self.assertEqual(self.err, str(err.exception))

    def test_tuple_size(self):
        with self.assertRaises(TypeError) as err:
            self.s.size = (1, 2, 4)
        self.assertEqual(self.err, str(err.exception))

    def test_list_size(self):
        with self.assertRaises(TypeError) as err:
            self.s.size = [1, 2, 3]
        self.assertEqual(self.err, str(err.exception))

    def test_range_size(self):
        with self.assertRaises(TypeError) as err:
            self.s.size = range(5)
        self.assertEqual(self.err, str(err.exception))

    def test_dictionary_size(self):
        with self.assertRaises(TypeError) as err:
            self.s.size = {"a": 1, "b": 2}
        self.assertEqual(self.err, str(err.exception))

    def test_bool_size(self):
        with self.assertRaises(TypeError) as err:
            self.s.size = True
        self.assertEqual(self.err, str(err.exception))

    def test_set_size(self):
        with self.assertRaises(TypeError) as err:
            self.s.size = {"a", "b", "c", 3}
        self.assertEqual(self.err, str(err.exception))

    def test_frozenset_size(self):
        with self.assertRaises(TypeError) as err:
            self.s.size = frozenset({"a", "fixed", "set"})
        self.assertEqual(self.err, str(err.exception))

    def test_bytes_size(self):
        with self.assertRaises(TypeError) as err:
            self.s.size = b'n_bytes'
        self.assertEqual(self.err, str(err.exception))

    def test_memoryview_size(self):
        with self.assertRaises(TypeError) as err:
            self.s.size = memoryview(b'I see')
        self.assertEqual(self.err, str(err.exception))

    def test_nan_size(self):
        with self.assertRaises(TypeError) as err:
            self.s.size = float("nan")
        self.assertEqual(self.err, str(err.exception))

    def test_inf_size(self):
        with self.assertRaises(TypeError) as err:
            self.s.size = float("inf")
        self.assertEqual(self.err, str(err.exception))


class TestSquare_Update(unittest.TestCase):
    """Unittest for the update method of the class Square."""

    def test_empty_args(self):
        r = Square(5)
        r.update(*())
        self.assertEqual(str(r), f"[Square] ({r.id}) 0/0 - 5")

    def test_one_arg(self):
        r = Square(5)
        r.update(10)
        self.assertEqual(str(r), "[Square] (10) 0/0 - 5")

    def test_two_args(self):
        r = Square(5)
        r.update(1, 2)
        self.assertEqual(str(r), "[Square] (1) 0/0 - 2")

    def test_three_args(self):
        r = Square(5)
        r.update(1, 2, 3)
        self.assertEqual(str(r), "[Square] (1) 3/0 - 2")

    def test_four_args(self):
        r = Square(5)
        r.update(1, 2, 3, 4)
        self.assertEqual(str(r), "[Square] (1) 3/4 - 2")

    def test_more_than_four_args(self):
        r = Square(5)
        r.update(1, 2, 3, 4, 30, 23, 25)
        self.assertEqual(str(r), "[Square] (1) 3/4 - 2")

    def test_no_attribute(self):
        r = Square(5)
        r.update(**{})
        self.assertEqual(str(r), f"[Square] ({r.id}) 0/0 - 5")

    def test_one_attribute(self):
        r = Square(5)
        r.update(size=1)
        self.assertEqual(str(r), f"[Square] ({r.id}) 0/0 - 1")

    def test_two_attributes(self):
        r = Square(5)
        r.update(size=1, x=2)
        self.assertEqual(str(r), f"[Square] ({r.id}) 2/0 - 1")

    def test_three_attributes(self):
        r = Square(5)
        r.update(size=10, x=2, y=1)
        self.assertEqual(str(r), f"[Square] ({r.id}) 2/1 - 10")

    def test_four_attributes(self):
        r = Square(5)
        r.update(y=1, size=2, x=3, id=89)
        self.assertEqual(str(r), f"[Square] ({89}) 3/1 - 2")

    def test_not_present_attribute(self):
        r = Square(5)
        r.update(angle=90)
        self.assertEqual(str(r), f"[Square] ({r.id}) 0/0 - 5")

    def test_args_and_kwargs(self):
        r = Square(5)
        r.update(89, 2, size=30, x=40, y=100)
        self.assertEqual(str(r), "[Square] (89) 0/0 - 2")


class TestSquare_ToDictionary(unittest.TestCase):
    """Unittest for to_dictionary method of the class Square."""

    def test_todict(self):
        r = Square(1)
        r_dict = {
                "id": r.id,
                "size": 1,
                "x": 0,
                "y": 0
                }
        self.assertDictEqual(r.to_dictionary(), r_dict)

    def test_todict_x(self):
        r = Square(1, 2)
        r_dict = {
                "id": r.id,
                "size": 1,
                "x": 2,
                "y": 0
                }
        self.assertDictEqual(r.to_dictionary(), r_dict)

    def test_todict_y(self):
        r = Square(1, 0, 3)
        r_dict = {
                "id": r.id,
                "size": 1,
                "x": 0,
                "y": 3
                }
        self.assertDictEqual(r.to_dictionary(), r_dict)

    def test_todict_x_y(self):
        r = Square(1, 2, 3)
        r_dict = {
                "id": r.id,
                "size": 1,
                "x": 2,
                "y": 3
                }
        self.assertDictEqual(r.to_dictionary(), r_dict)

    def test_todict_x_y_id(self):
        r = Square(1, 2, 3, 4)
        r_dict = {
                "id": 4,
                "size": 1,
                "x": 2,
                "y": 3
                }
        self.assertDictEqual(r.to_dictionary(), r_dict)

    def test_todict_id_None(self):
        r = Square(1, 2, 3, 4)
        r.id = None
        r_dict = {
                "id": None,
                "size": 1,
                "x": 2,
                "y": 3
                }
        self.assertDictEqual(r.to_dictionary(), r_dict)


class TestSquare___Str__(unittest.TestCase):
    """Unittest for __str__ magic method of the class Square."""

    def test__str__(self):
        r = Square(3, 4, 1, 2)
        str_r = f"[Square] (2) 4/1 - 3"
        self.assertEqual(str_r, str(r))

    @unittest.mock.patch("sys.stdout", new_callable=StringIO)
    def test_stdout(self, mock_stdout):
        r = Square(3, 4, 1, 2)
        print(r)
        self.assertEqual(mock_stdout.getvalue(), str(r) + "\n")


if __name__ == '__main__':
    unittest.main()
