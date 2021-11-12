#!/usr/bin/python3
"""
Testing the user (user.py) model.
"""
import unittest
from models.city import City, BaseModel


class Test_modules(unittest.TestCase):
    """
    Testing modules: state
    """
    def test_City(self):
        """
        Testing State: 'name' class attribute
        """
        self.assertTrue(issubclass(City, BaseModel))
        self.assertTrue(type(City.name) == str)
        self.assertTrue(type(City.state_id) == str)


if __name__ == '__main__':
    unittest.main()
