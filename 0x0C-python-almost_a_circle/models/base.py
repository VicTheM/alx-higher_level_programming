#!/usr/bin/python3
"""Defines a Base class."""
import json
import csv


class Base:
    """Represents a base model"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an instance of Base.

        Args:
            id (:obj: `int`, optional): The id of instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of a list of dictionaries."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        filename = f"{cls.__name__}.json"
        list_dictionaries = []
        if list_objs is None:
            pass
        else:
            for obj in list_objs:
                list_dictionaries.append(obj.to_dictionary())

        json_string = cls.to_json_string(list_dictionaries)
        with open(filename, mode="w", encoding="utf-8") as json_file:
            json_file.write(json_string)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the csv of list_objs to a file."""
        filename = f"{cls.__name__}.csv"
        list_dictionaries = []
        if list_objs is None:
            pass
        else:
            for obj in list_objs:
                list_dictionaries.append(obj.to_dictionary())

        with open(filename, mode="w", encoding="utf-8") as csv_file:
            if list_dictionaries == []:
                csv_file.write("[]")
                return
            fieldnames = list_dictionaries[0].keys()
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            for dict_obj in list_dictionaries:
                csv_writer.writerow(dict_obj)

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances from class csv file."""
        filename = f"{cls.__name__}.csv"
        list_objs = []
        try:
            with open(filename, encoding="utf-8") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for dictionary in csv_reader:
                    for key, value in dictionary.items():
                        dictionary[key] = int(value)
                    list_objs.append(cls.create(**dictionary))
        except FileNotFoundError:
            pass
        return list_objs

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from class json file."""
        filename = f"{cls.__name__}.json"
        list_objs = []
        try:
            with open(filename, encoding="utf-8") as json_file:
                list_dictionaries = cls.from_json_string(json_file.read())
            for dictionary in list_dictionaries:
                list_objs.append(cls.create(**dictionary))
        except FileNotFoundError:
            pass
        return list_objs
