#!/usr/bin/python3
"""
Testing the file_storage model.
"""
import json
from models.engine.file_storage import FileStorage
import unittest
from models.base_model import BaseModel


class Test_FileStorage(unittest.TestCase):
    """
    Testing models.file_storage model.
    """

    def test_all(self):
        """
        Testing the `all` method:
        Must return __objects dictionary
        """
        storage = FileStorage()
        obj = storage.all()
        self.assertEqual(type(obj), dict,
                         "the returned object must be a dictionary")

    def test_new(self):
        """
        Testing the `new` method:
        Must sets in __objects the BaseModel obj with key <obj class name>.id
        """
        my_model = BaseModel()
        storage = FileStorage()

        my_model_ID = my_model.id
        my_model_Class = my_model.__class__.__name__
        storage.new(my_model)
        Dict = storage.all()
        self.assertEqual(Dict['.'.join((my_model_Class, my_model_ID))],
                         my_model)


if __name__ == '__main__':
    unittest.main()
