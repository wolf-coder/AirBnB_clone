"""
Main Module
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Class that defines all common attributes/methods for other classes.
    """
    def __init__(self):
        """
        Instance initialisation
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        Updates the public instance attribute updated_at with the current
        datetime
        """
        self.updated_at = datetime.now()

    def __str__(self):
        """
        print: [<class name>] (<self.id>) <self.__dict__>
        """
        return ''.join(["[BaseModel] ",
                        "(", self.id, ") ",
                        str(self.__dict__)])

    def to_dict(self):
        """
        >> This method will be the first piece of the
        serialization/deserialization process:
        >> create a dictionary representation with
        “simple object type” of the BaseModel
        """
        setattr(self, 'created_at', self.created_at.isoformat())
        setattr(self, 'updated_at', self.updated_at.isoformat())
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__
