#!/usr/bin/python3
"""
Testing the user (user.py) model.
"""
import unittest
from models.amenity import Amenity


class Test_modules(unittest.TestCase):
    """
    Testing modules: amenity, city, places, review, stat
    """
    def test_Amenity(self):
        """
        Testing Amenity: 'name' class attribute
        """
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertIn("name", Amenity.__dict__)


if __name__ == '__main__':
    unittest.main()
