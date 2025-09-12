#!/usr/bin/python3
"""Base model for spmjp"""
import uuid
from datetime import datetime
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

time = "%Y-%m-%dT%H:%M:%S.%f"

if models.storage_t == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """Class from which all other classes will inherit"""
    if models.storage_t == "db":
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
        updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """ Initialisation of base_model """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Return string representation """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__)

    def save(self):
        """Updates public instance attribute updated_at 
          with current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self, save_fs=None):
        """ Returns a dictionary containing all keys/values of
        the instance """
        my_dict = self.__dict__.copy()
        if "created_at" in my_dict:
            my_dict["created_at"] = my_dict["created_at"].strftime(time)
        if "updated_at" in my_dict:
            my_dict["updated_at"] = my_dict["updated_at"].strftime(time)
        my_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in my_dict:
            del my_dict["_sa_instance_state"]
        if save_fs is None:
            if "password" in my_dict:
                del my_dict["password"]
        return my_dict

    def delete(self):
        """ Delete current instance from storage """
        models.storage.delete(self)
