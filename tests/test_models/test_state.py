#!/usr/bin/python3
"""
Testing the user (user.py) model.
"""
import unittest
from models.state import State, BaseModel


class Test_modules(unittest.TestCase):
    """
    Testing modules: state
    """
    def test_State(self):
        """
        Testing State: 'name' class attribute
        """
        self.assertTrue(issubclass(State, BaseModel))
        self.assertIn("name", State.__dict__)


if __name__ == '__main__':
    unittest.main()
