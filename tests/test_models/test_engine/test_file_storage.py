#!/usr/bin/python3
"""
Testing the file_storage model.
"""
import json
from models.engine.file_storage import FileStorage
import unittest
from models.base_model import BaseModel
from io import StringIO


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

    def test_save(self):
        """
        This method must serializes __objects to the JSON file
        (path: __file_path)
        TODO:THE FOLLOWING TEST IS NOT VALID
        """
        my_model = BaseModel()
        storage = FileStorage()

        my_model_ID = my_model.id
        my_model_Class = my_model.__class__.__name__
        storage.new(my_model)
        storage.save()
        Dict = storage.all()
        self.assertEqual(Dict['.'.join((my_model_Class, my_model_ID))],
                         my_model)

    def test_reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        my_model = BaseModel()
        storage = FileStorage()

        my_model_ID = my_model.id
        my_model_Class = my_model.__class__.__name__
        storage.new(my_model)
        storage.save()
        Dict_before_reload = storage.all()
        storage.reload()
        Dict_after_reload = storage.all()
        self.assertCountEqual(Dict_after_reload.keys(),
                              Dict_before_reload.keys())


if __name__ == '__main__':
    unittest.main()
