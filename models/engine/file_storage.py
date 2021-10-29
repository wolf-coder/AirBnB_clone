#!/usr/bin/python3
"""
data storage manipulation
"""
import json
from models.base_model import BaseModel


class FileStorage():
    """
    Serializes instances to a JSON file
    and
    deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        self.__objects['.'.join((obj.__class__.__name__, obj.id))] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        _Dict = {}
        for k, v in self.all().items():
            _Dict[k] = v.to_dict()
        with open(self.__file_path, 'w') as fd:
            json.dump(_Dict, fd)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r')as fp:
                _Dict = json.load(fp)
                self.__objects = {k: BaseModel(**v) for k, v in _Dict.items()}
        except FileNotFoundError:
            pass
