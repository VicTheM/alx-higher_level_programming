#!/usr/bin/python3
"""Defines a Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the Square

        Args:
            size (int): The size of the Square.
            x (:obj:`int`, optional): The amount of space from the left.
            y (:obj:`int`, optional): The amount of space up top.
            id (:obj:`int`, optional): The Rectagle id.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets/Sets the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the Square."""
        if len(args) > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of the Square."""
        attrbs = {}
        for key, value in self.__dict__.items():
            if "_" in key:
                key = key.split("_")[-1]
            if key in ["width", "height"]:
                key = "size"
            attrbs[key] = value
        return attrbs

    def __str__(self):
        """Returns the string representation of the Square."""
        msg = "[Square] ({}) {}/{} - {}"
        return msg.format(self.id, self.x, self.y, self.size)
