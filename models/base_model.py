#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """Base class for models"""

    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel class."""

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at ' or key == 'updated_at':
                    time_f = '%Y-%m-%dT%H:%M:%S.%f'
                    value = datetime.strptime(value, time_f)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__})]"

    def save(self):
        """Update the 'updated_at' attribute"""
        self.updated_at = datetime.now()
        models.storage.save() 

    def to_dict(self):
        """Converts the instance to a dictionary representation."""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary
