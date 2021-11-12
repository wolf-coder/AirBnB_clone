#!/usr/bin/python3
"""
Testing the user (user.py) model.
"""
import unittest
from models.review import Review, BaseModel


class Test_modules(unittest.TestCase):
    """
    Testing modules: state
    """
    def test_Review(self):
        """
        Testing State: 'name' class attribute
        """
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertTrue(type("place_id") == str)
        self.assertTrue(type("user_id") == str)
        self.assertTrue(type("text") == str)


if __name__ == '__main__':
    unittest.main()
