#!/usr/bin/python3
"""BaseModel module"""
import uuid
from datetime import datetime
import models
from sqlalchemy import Column, Integer, String, DateTime, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel:
    """BaseModel class"""
    id = Column(String(60), nullable=False, unique=True, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialization of model"""
        if kwargs is not None and kwargs != {}:
            del kwargs["__class__"]
            for key in kwargs.keys():
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """string representation of an instance"""
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """update the public instance attribute"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Serialize object to JSON"""
        obj_dict = self.__dict__.copy()
        if "_sa_instance_state" in obj_dict.keys():
            del obj_dict["_sa_instance_state"]
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
