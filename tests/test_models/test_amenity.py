#!/usr/bin/python3
"""
Testing the user (user.py) model.
"""
import unittest
from models.amenity import Amenity, BaseModel


class Test_modules(unittest.TestCase):
    """
    Testing modules: state
    """
    def test_Amenity(self):
        """
        Testing State: 'name' class attribute
        """
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertIn("name", Amenity.__dict__)
        self.assertTrue(type(Amenity.name) == str)


if __name__ == '__main__':
    unittest.main()
