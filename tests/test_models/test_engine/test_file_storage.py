#!/usr/bin/python3
"""
Testing the file_storage model.
"""
import json
from models.engine.file_storage import FileStorage
import unittest


class Test_FileStorage(unittest.TestCase):
    """
    Testing models.file_storage model.
    """

    def test_all(self):
        """
        Testing the `all` method:
        must return __objects dictionary
        """
        storage = FileStorage()
        obj = storage.all()
        self.assertEqual(type(obj), dict,
                         "the returned object must be a dictionary")


if __name__ == '__main__':
    unittest.main()
