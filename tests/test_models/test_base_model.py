#!/usr/bin/python3
"""
Testing the base_model model.
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class Test_Base_Model(unittest.TestCase):
    """
    models/base_model Testing
    """

    def test0(self):
        """
        Testing the to_dict() methods output
        """
        Instance = BaseModel()
        ToDict = Instance.to_dict()
        self.assertEqual(type(ToDict['created_at']), str)
        self.assertEqual(type(ToDict['updated_at']), str)


if __name__ == '__main__':
    unittest.main()
