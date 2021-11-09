#!/usr/bin/python3
"""
Testing the user (user.py) model.
"""
import unittest
from models.user import User, BaseModel


class Test_User(unittest.TestCase):
    """
    Testing models.User model.
    """
    def test_inheritance(self):
        """
        Testing User inherit from BaseModel
        """
        self.assertTrue(issubclass(User, BaseModel))
        self.assertTrue(type(User.first_name), "")


if __name__ == '__main__':
    unittest.main()
