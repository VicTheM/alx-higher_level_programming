#!/usr/bin/python3
"""unittest for Rectangle class.

    TestRectangle_Initialization - line 22
    TestRectangle_Width - line 130
    TestRectangle_Height - line 222
    TestRectangle_X - line 314
    TestRectangle_Y - line 404
    TestRectangle_Area - line 494
    TestRectangle_Display - line 510
    TestRectangle_Update - line 539
    TestRectangle_ToDictionary - line 617
    TestRectangle___Str__  - line 688
"""
import models
import unittest
import unittest.mock
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_Documentation(unittest.TestCase):
    """Unittest for the documentation."""

    def test_rectangle_module(self):
        self.assertIsNotNone(models.rectangle.__doc__)
        self.assertNotEqual(models.rectangle.__doc__, "")

    def test_rectagle_class(self):
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertNotEqual(Rectangle.__doc__, "")

    def test_area_method(self):
        self.assertIsNotNone(Rectangle.area.__doc__)
        self.assertNotEqual(Rectangle.area.__doc__, "")

    def test_display_method(self):
        self.assertIsNotNone(Rectangle.display.__doc__)
        self.assertNotEqual(Rectangle.display.__doc__, "")

    def test_update_method(self):
        self.assertIsNotNone(Rectangle.update.__doc__)
        self.assertNotEqual(Rectangle.update.__doc__, "")

    def test_to_dictionary_method(self):
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__)
        self.assertNotEqual(Rectangle.to_dictionary.__doc__, "")

    def test___str___method(self):
        self.assertIsNotNone(Rectangle.__str__.__doc__)
        self.assertNotEqual(Rectangle.__str__.__doc__, "")


class TestRectangle_Initialization(unittest.TestCase):
    """Unittest for the initialization of the class Rectangle."""

    def test_isinstance_Base(self):
        self.assertIsInstance(Rectangle(2, 4), Base)

    def test_zero_arg(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1,)

    def test_two_args(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertIsNot(r1, r2)

    def test_three_arg3(self):
        r1 = Rectangle(1, 2, 3)
        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertIsNot(r1, r2)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertIsNot(r1, r2)

    def test_five_args(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.id, r2.id)
        self.assertIsNot(r1, r2)

    def test_more_than_five_args(self):
        with self.subTest("6"):
            with self.assertRaises(TypeError):
                Rectangle(1, 2, 3, 4, 5, 6)
        with self.subTest("7"):
            with self.assertRaises(TypeError):
                Rectangle(1, 2, 3, 4, 5, 6, 7)

    def test_width_getter(self):
        r = Rectangle(6, 4)
        self.assertEqual(r.width, 6)

    def test_width_setter(self):
        r = Rectangle(6, 4)
        r.width = 24
        self.assertEqual(r.width, 24)

    def test_height_getter(self):
        r = Rectangle(5, 2)
        self.assertEqual(r.height, 2)

    def test_height_setter(self):
        r = Rectangle(5, 2)
        r.height = 10
        self.assertEqual(r.height, 10)

    def test_x_getter(self):
        r = Rectangle(3, 1, 7)
        self.assertEqual(r.x, 7)

    def test_x_setter(self):
        r = Rectangle(3, 1, 7)
        r.x = 21
        self.assertEqual(r.x, 21)

    def test_y_getter(self):
        r = Rectangle(2, 3, 1)
        self.assertEqual(r.y, 0)

    def test_y_getter(self):
        r = Rectangle(2, 3, 1)
        r.y = 6
        self.assertEqual(r.y, 6)

    def test_id(self):
        r = Rectangle(1, 3, 4)
        r.id = 104
        self.assertEqual(r.id, 104)

    def test_private_width(self):
        r = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            r.__width

    def test_private_height(self):
        r = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            r.__height

    def test_private_x(self):
        r = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            r.__x

    def test_private_x(self):
        r = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            r.__y


class TestRectangle_Width(unittest.TestCase):
    """Unittest for the width attribute of the class Rectangle."""

    def setUp(self):
        self.r = Rectangle(1, 1)
        self.err = "width must be an integer"
        self.err1 = "width must be > 0"

    def test_int_width(self):
        self.r.width = 2

    def test_negative_int_width(self):
        with self.assertRaises(ValueError) as err:
            self.r.width = -3
        self.assertEqual(self.err1, str(err.exception))

    def test_zero_width(self):
        with self.assertRaises(ValueError) as err:
            self.r.width = 0
        self.assertEqual(self.err1, str(err.exception))

    def test_float_width(self):
        with self.assertRaises(TypeError) as err:
            self.r.width = 2.5
        self.assertEqual(self.err, str(err.exception))

    def test_complex_width(self):
        with self.assertRaises(TypeError) as err:
            self.r.width = 2 + 7j
        self.assertEqual(self.err, str(err.exception))

    def test_string_width(self):
        with self.assertRaises(TypeError) as err:
            self.r.width = "2"
        self.assertEqual(self.err, str(err.exception))

    def test_tuple_width(self):
        with self.assertRaises(TypeError) as err:
            self.r.width = (1, 2, 4)
        self.assertEqual(self.err, str(err.exception))

    def test_list_width(self):
        with self.assertRaises(TypeError) as err:
            self.r.width = [1, 2, 3]
        self.assertEqual(self.err, str(err.exception))

    def test_range_width(self):
        with self.assertRaises(TypeError) as err:
            self.r.width = range(5)
        self.assertEqual(self.err, str(err.exception))

    def test_dictionary_width(self):
        with self.assertRaises(TypeError) as err:
            self.r.width = {"a": 1, "b": 2}
        self.assertEqual(self.err, str(err.exception))

    def test_bool_width(self):
        with self.assertRaises(TypeError) as err:
            self.r.width = True
        self.assertEqual(self.err, str(err.exception))

    def test_set_width(self):
        with self.assertRaises(TypeError) as err:
            self.r.width = {"a", "b", "c", 3}
        self.assertEqual(self.err, str(err.exception))

    def test_frozenset_width(self):
        with self.assertRaises(TypeError) as err:
            self.r.width = frozenset({"a", "fixed", "set"})
        self.assertEqual(self.err, str(err.exception))

    def test_bytes_width(self):
        with self.assertRaises(TypeError) as err:
            self.r.width = b'n_bytes'
        self.assertEqual(self.err, str(err.exception))

    def test_memoryview_width(self):
        with self.assertRaises(TypeError) as err:
            self.r.width = memoryview(b'I see')
        self.assertEqual(self.err, str(err.exception))

    def test_nan_width(self):
        with self.assertRaises(TypeError) as err:
            self.r.width = float("nan")
        self.assertEqual(self.err, str(err.exception))

    def test_inf_width(self):
        with self.assertRaises(TypeError) as err:
            self.r.width = float("inf")
        self.assertEqual(self.err, str(err.exception))


class TestRectangle_Height(unittest.TestCase):
    """Unittest for the height attribute of the class Rectangle."""

    def setUp(self):
        self.r = Rectangle(1, 1)
        self.err = "height must be an integer"
        self.err1 = "height must be > 0"

    def test_int_height(self):
        self.r.height = 2

    def test_negative_int_height(self):
        with self.assertRaises(ValueError) as err:
            self.r.height = -3
        self.assertEqual(self.err1, str(err.exception))

    def test_zero_height(self):
        with self.assertRaises(ValueError) as err:
            self.r.height = 0
        self.assertEqual(self.err1, str(err.exception))

    def test_float_height(self):
        with self.assertRaises(TypeError) as err:
            self.r.height = 2.5
        self.assertEqual(self.err, str(err.exception))

    def test_complex_height(self):
        with self.assertRaises(TypeError) as err:
            self.r.height = 2 + 7j
        self.assertEqual(self.err, str(err.exception))

    def test_string_height(self):
        with self.assertRaises(TypeError) as err:
            self.r.height = "2"
        self.assertEqual(self.err, str(err.exception))

    def test_tuple_height(self):
        with self.assertRaises(TypeError) as err:
            self.r.height = (1, 2, 4)
        self.assertEqual(self.err, str(err.exception))

    def test_list_height(self):
        with self.assertRaises(TypeError) as err:
            self.r.height = [1, 2, 3]
        self.assertEqual(self.err, str(err.exception))

    def test_range_height(self):
        with self.assertRaises(TypeError) as err:
            self.r.height = range(5)
        self.assertEqual(self.err, str(err.exception))

    def test_dictionary_height(self):
        with self.assertRaises(TypeError) as err:
            self.r.height = {"a": 1, "b": 2}
        self.assertEqual(self.err, str(err.exception))

    def test_bool_height(self):
        with self.assertRaises(TypeError) as err:
            self.r.height = True
        self.assertEqual(self.err, str(err.exception))

    def test_set_height(self):
        with self.assertRaises(TypeError) as err:
            self.r.height = {"a", "b", "c", 3}
        self.assertEqual(self.err, str(err.exception))

    def test_frozenset_height(self):
        with self.assertRaises(TypeError) as err:
            self.r.height = frozenset({"a", "fixed", "set"})
        self.assertEqual(self.err, str(err.exception))

    def test_bytes_height(self):
        with self.assertRaises(TypeError) as err:
            self.r.height = b'n_bytes'
        self.assertEqual(self.err, str(err.exception))

    def test_memoryview_height(self):
        with self.assertRaises(TypeError) as err:
            self.r.height = memoryview(b'I see')
        self.assertEqual(self.err, str(err.exception))

    def test_nan_height(self):
        with self.assertRaises(TypeError) as err:
            self.r.height = float("nan")
        self.assertEqual(self.err, str(err.exception))

    def test_inf_height(self):
        with self.assertRaises(TypeError) as err:
            self.r.height = float("inf")
        self.assertEqual(self.err, str(err.exception))


class TestRectangle_X(unittest.TestCase):
    """Unittest for the x attribute of the class Rectangle."""

    def setUp(self):
        self.r = Rectangle(1, 1)
        self.err = "x must be an integer"
        self.err1 = "x must be >= 0"

    def test_int_x(self):
        self.r.x = 2

    def test_negative_int_x(self):
        with self.assertRaises(ValueError) as err:
            self.r.x = -3
        self.assertEqual(self.err1, str(err.exception))

    def test_zero_x(self):
        self.r.x = 0

    def test_float_x(self):
        with self.assertRaises(TypeError) as err:
            self.r.x = 2.5
        self.assertEqual(self.err, str(err.exception))

    def test_complex_x(self):
        with self.assertRaises(TypeError) as err:
            self.r.x = 2 + 7j
        self.assertEqual(self.err, str(err.exception))

    def test_string_x(self):
        with self.assertRaises(TypeError) as err:
            self.r.x = "2"
        self.assertEqual(self.err, str(err.exception))

    def test_tuple_x(self):
        with self.assertRaises(TypeError) as err:
            self.r.x = (1, 2, 4)
        self.assertEqual(self.err, str(err.exception))

    def test_list_x(self):
        with self.assertRaises(TypeError) as err:
            self.r.x = [1, 2, 3]
        self.assertEqual(self.err, str(err.exception))

    def test_range_x(self):
        with self.assertRaises(TypeError) as err:
            self.r.x = range(5)
        self.assertEqual(self.err, str(err.exception))

    def test_dictionary_x(self):
        with self.assertRaises(TypeError) as err:
            self.r.x = {"a": 1, "b": 2}
        self.assertEqual(self.err, str(err.exception))

    def test_bool_x(self):
        with self.assertRaises(TypeError) as err:
            self.r.x = True
        self.assertEqual(self.err, str(err.exception))

    def test_set_x(self):
        with self.assertRaises(TypeError) as err:
            self.r.x = {"a", "b", "c", 3}
        self.assertEqual(self.err, str(err.exception))

    def test_frozenset_x(self):
        with self.assertRaises(TypeError) as err:
            self.r.x = frozenset({"a", "fixed", "set"})
        self.assertEqual(self.err, str(err.exception))

    def test_bytes_x(self):
        with self.assertRaises(TypeError) as err:
            self.r.x = b'n_bytes'
        self.assertEqual(self.err, str(err.exception))

    def test_memoryview_x(self):
        with self.assertRaises(TypeError) as err:
            self.r.x = memoryview(b'I see')
        self.assertEqual(self.err, str(err.exception))

    def test_nan_x(self):
        with self.assertRaises(TypeError) as err:
            self.r.x = float("nan")
        self.assertEqual(self.err, str(err.exception))

    def test_inf_x(self):
        with self.assertRaises(TypeError) as err:
            self.r.x = float("inf")
        self.assertEqual(self.err, str(err.exception))


class TestRectangle_Y(unittest.TestCase):
    """Unittest for the y attribute of the class Rectangle."""

    def setUp(self):
        self.r = Rectangle(1, 1)
        self.err = "y must be an integer"
        self.err1 = "y must be >= 0"

    def test_int_y(self):
        self.r.y = 2

    def test_negative_int_y(self):
        with self.assertRaises(ValueError) as err:
            self.r.y = -3
        self.assertEqual(self.err1, str(err.exception))

    def test_zero_y(self):
        self.r.y = 0

    def test_float_y(self):
        with self.assertRaises(TypeError) as err:
            self.r.y = 2.5
        self.assertEqual(self.err, str(err.exception))

    def test_compley_y(self):
        with self.assertRaises(TypeError) as err:
            self.r.y = 2 + 7j
        self.assertEqual(self.err, str(err.exception))

    def test_string_y(self):
        with self.assertRaises(TypeError) as err:
            self.r.y = "2"
        self.assertEqual(self.err, str(err.exception))

    def test_tuple_y(self):
        with self.assertRaises(TypeError) as err:
            self.r.y = (1, 2, 4)
        self.assertEqual(self.err, str(err.exception))

    def test_list_y(self):
        with self.assertRaises(TypeError) as err:
            self.r.y = [1, 2, 3]
        self.assertEqual(self.err, str(err.exception))

    def test_range_y(self):
        with self.assertRaises(TypeError) as err:
            self.r.y = range(5)
        self.assertEqual(self.err, str(err.exception))

    def test_dictionary_y(self):
        with self.assertRaises(TypeError) as err:
            self.r.y = {"a": 1, "b": 2}
        self.assertEqual(self.err, str(err.exception))

    def test_bool_y(self):
        with self.assertRaises(TypeError) as err:
            self.r.y = True
        self.assertEqual(self.err, str(err.exception))

    def test_set_y(self):
        with self.assertRaises(TypeError) as err:
            self.r.y = {"a", "b", "c", 3}
        self.assertEqual(self.err, str(err.exception))

    def test_frozenset_y(self):
        with self.assertRaises(TypeError) as err:
            self.r.y = frozenset({"a", "fixed", "set"})
        self.assertEqual(self.err, str(err.exception))

    def test_bytes_y(self):
        with self.assertRaises(TypeError) as err:
            self.r.y = b'n_bytes'
        self.assertEqual(self.err, str(err.exception))

    def test_memoryview_y(self):
        with self.assertRaises(TypeError) as err:
            self.r.y = memoryview(b'I see')
        self.assertEqual(self.err, str(err.exception))

    def test_nan_y(self):
        with self.assertRaises(TypeError) as err:
            self.r.y = float("nan")
        self.assertEqual(self.err, str(err.exception))

    def test_inf_y(self):
        with self.assertRaises(TypeError) as err:
            self.r.y = float("inf")
        self.assertEqual(self.err, str(err.exception))


class TestRectangle_Area(unittest.TestCase):
    """Unittest for the initialization of the class Rectangle."""

    def test_area_1(self):
        r = Rectangle(2, 4)
        self.assertEqual(r.area(), 2 * 4)

    def test_area_2(self):
        r = Rectangle(200, 400)
        self.assertEqual(r.area(), 200 * 400)

    def test_area_3(self):
        r = Rectangle(1, 1)
        self.assertEqual(r.area(), 1)


class TestRectangle_Display(unittest.TestCase):
    """Unittest for the display method of the class Rectangle."""

    @unittest.mock.patch("sys.stdout", new_callable=StringIO)
    def test_display(self, mock_stdout):
        r = Rectangle(2, 4)
        r.display()
        self.assertEqual(mock_stdout.getvalue(), "##\n##\n##\n##\n")

    @unittest.mock.patch("sys.stdout", new_callable=StringIO)
    def test_display_x(self, mock_stdout):
        r = Rectangle(2, 4, 2)
        r.display()
        self.assertEqual(mock_stdout.getvalue(), "  ##\n  ##\n  ##\n  ##\n")

    @unittest.mock.patch("sys.stdout", new_callable=StringIO)
    def test_display_y(self, mock_stdout):
        r = Rectangle(2, 4, 0, 2)
        r.display()
        self.assertEqual(mock_stdout.getvalue(), "\n\n##\n##\n##\n##\n")

    @unittest.mock.patch("sys.stdout", new_callable=StringIO)
    def test_display_x_y(self, mock_stdout):
        r = Rectangle(2, 4, 2, 2)
        r.display()
        output = "\n\n  ##\n  ##\n  ##\n  ##\n"
        self.assertEqual(mock_stdout.getvalue(), output)


class TestRectangle_Update(unittest.TestCase):
    """Unittest for the update method of the class Rectangle."""
    def test_empty_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(*())
        self.assertEqual(str(r), f"[Rectangle] ({r.id}) 10/10 - 10/10")

    def test_one_arg(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")

    def test_two_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")

    def test_three_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")

    def test_four_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")

    def test_five_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_more_than_five_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 23, 25)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_empty_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(**{})
        self.assertEqual(str(r), f"[Rectangle] ({r.id}) 10/10 - 10/10")

    def test_one_kwarg(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(str(r), f"[Rectangle] ({r.id}) 10/10 - 10/1")

    def test_two_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(width=1, x=2)
        self.assertEqual(str(r), f"[Rectangle] ({r.id}) 2/10 - 1/10")

    def test_three_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(width=1, x=2, height=1)
        self.assertEqual(str(r), f"[Rectangle] ({r.id}) 2/10 - 1/1")

    def test_four_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), f"[Rectangle] ({r.id}) 3/1 - 2/10")

    def test_five_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(y=1, width=2, x=3, id=89, height=1)
        self.assertEqual(str(r), f"[Rectangle] ({r.id}) 3/1 - 2/1")

    def test_not_present_attribute(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(angle=90)
        self.assertEqual(str(r), f"[Rectangle] ({r.id}) 10/10 - 10/10")

    def test_args_and_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, height=20, width=30)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")


class TestRectangle_ToDictionary(unittest.TestCase):
    """Unittest for to_dictionary method of the class Rectangle."""

    def test_todict(self):
        r = Rectangle(1, 2)
        r_dict = {
                "id": r.id,
                "width": 1,
                "height": 2,
                "x": 0,
                "y": 0
                }
        self.assertDictEqual(r.to_dictionary(), r_dict)

    def test_todict_x(self):
        r = Rectangle(1, 2, 3)
        r_dict = {
                "id": r.id,
                "width": 1,
                "height": 2,
                "x": 3,
                "y": 0
                }
        self.assertDictEqual(r.to_dictionary(), r_dict)

    def test_todict_y(self):
        r = Rectangle(1, 2, 0, 3)
        r_dict = {
                "id": r.id,
                "width": 1,
                "height": 2,
                "x": 0,
                "y": 3
                }
        self.assertDictEqual(r.to_dictionary(), r_dict)

    def test_todict_x_y(self):
        r = Rectangle(1, 2, 3, 4)
        r_dict = {
                "id": r.id,
                "width": 1,
                "height": 2,
                "x": 3,
                "y": 4
                }
        self.assertDictEqual(r.to_dictionary(), r_dict)

    def test_todict_x_y_id(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r_dict = {
                "id": 5,
                "width": 1,
                "height": 2,
                "x": 3,
                "y": 4
                }
        self.assertDictEqual(r.to_dictionary(), r_dict)

    def test_todict_id_None(self):
        r = Rectangle(1, 2, 3, 4)
        r.id = None
        r_dict = {
                "id": None,
                "width": 1,
                "height": 2,
                "x": 3,
                "y": 4
                }
        self.assertDictEqual(r.to_dictionary(), r_dict)


class TestRectangle___Str__(unittest.TestCase):
    """Unittest for __str__ magic method of the class Rectangle."""

    def test__str__(self):
        r = Rectangle(3, 4, 1, 2)
        str_r = f"[Rectangle] ({r.id}) 1/2 - 3/4"
        self.assertEqual(str_r, str(r))

    @unittest.mock.patch("sys.stdout", new_callable=StringIO)
    def test_stdout(self, mock_stdout):
        r = Rectangle(3, 4, 1, 2)
        print(r)
        self.assertEqual(mock_stdout.getvalue(), str(r) + "\n")


if __name__ == '__main__':
    unittest.main()
