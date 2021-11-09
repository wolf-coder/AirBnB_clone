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
        self.assertIn("email", User.__dict__)
        self.assertIn("password", User.__dict__)
        self.assertIn("first_name", User.__dict__)
        self.assertIn("last_name", User.__dict__)


if __name__ == '__main__':
    unittest.main()
