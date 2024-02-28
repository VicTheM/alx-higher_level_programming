#!/usr/bin/python3
""" CLASSES / JSON """

class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if isinstance(attrs, list) and \
                all(isinstance(item, str) for item in attrs):
            attributes = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    attributes[key] = value
            return attributes
        return self.__dict__

    def reload_from_json(self, json):
        """Refreshes all instance variables from a dictionary"""
        for key, value in self.__dict__.items():
            self.__dict__[key] = json[key]

