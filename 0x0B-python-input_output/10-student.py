#!/usr/bin/python3
<<<<<<< HEAD
=======
<<<<<<< HEAD
"""class Student that defines a student by:
Public instance attributes:
first_name
last_name
age
"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
=======
>>>>>>> 5e672edc13e61c221d0d9bc6cd742692f5d6e566
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
<<<<<<< HEAD
=======
>>>>>>> 0f9335aeefad229f6daf32095d498cf8bbd11781
>>>>>>> 5e672edc13e61c221d0d9bc6cd742692f5d6e566
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
<<<<<<< HEAD
=======
<<<<<<< HEAD
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for item in attrs:
                if hasattr(self, item):
                    new_dict[item] = getattr(self, item)
            return new_dict
=======
>>>>>>> 5e672edc13e61c221d0d9bc6cd742692f5d6e566
        """Get a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
<<<<<<< HEAD
=======
>>>>>>> 0f9335aeefad229f6daf32095d498cf8bbd11781
>>>>>>> 5e672edc13e61c221d0d9bc6cd742692f5d6e566
