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
    models/base_model Testing:
    - All key values are str type.
    """

    def test_to_dict(self):
        """
        Testing the to_dict() methods.
        """
        Instance = BaseModel()
        ToDict = Instance.to_dict()
        self.assertEqual(type(ToDict['updated_at']), str)

    def test_save(self):
        """
        Testing the save() methods:
        - 'updated_at' attribute is updated.
        """

        Instance = BaseModel()
        Time_1 = Instance.updated_at
        Instance.save()
        Time_2 = Instance.updated_at
        self.assertNotEqual(Time_1, Time_2)

    def test_Magic_str(self):
        """
        Testing __str__() method:
        - output equal to: '[<class name>] (<self.id>) <self.__dict__>'
        """

        Instance = BaseModel()
        Requiered = "[BaseModel] ({}) {}".format(Instance.id,
                                                 Instance.__dict__)
        Result = Instance.__str__()
        self.assertEqual(Requiered, Result)


if __name__ == '__main__':
    unittest.main()
