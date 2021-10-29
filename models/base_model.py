#!/usr/bin/python3
"""
Main Module with the Main class
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Class that defines all common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Instance initialisation
        """
        if kwargs:
            for Key, Value in kwargs.items():
                if Key in ('created_at', 'updated_at'):
                    setattr(self, Key, datetime.strptime(
                        Value,
                        '%Y-%m-%dT%H:%M:%S.%f'))
                elif Key != '__class__':
                    setattr(self, Key, Value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            """
            The FileModels.Storage.new() method function definition:
            def new(self, obj)
            `self` here will be bound to `obj`
            """
            models.storage.new(self)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current
        datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """
        print: [<class name>] (<self.id>) <self.__dict__>
        """
        return ("[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__))

    def to_dict(self):
        """
        >> Method that creates a dictionary representation with
        "simple object type" of the BaseModel
        """
        Cpy = self.__dict__.copy()
        Cpy["created_at"] = self.created_at.isoformat()
        Cpy["updated_at"] = self.updated_at.isoformat()
        Cpy["__class__"] = self.__class__.__name__
        return Cpy
