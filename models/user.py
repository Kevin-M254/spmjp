#!/usr/bin/python3
""" Module for User """
from models.base_model import BaseModel, Base
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel, Base):
    """ Class for managing User objects
        Attributes:
            email (str): email of user.
            password (str): password of user
            username (str): username of user
    """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        username = Column(String(128), nullable=True)
        prediction = relationship("Prediction", backref="user")
    else:
        email = ""
        password = ""
        username = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """ Hashes password with md5 encryption """
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
