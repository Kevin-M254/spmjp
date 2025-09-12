#!/usr/bin/python3
""" Module for League class """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class League(BaseModel, Base):
    """ Class for managing League objects
        Attributes:
            country_id (str): the country id
            name (str): name of league
    """
    if models.storage_t == "db":
        __tablename__ = "leagues"
        country_id = Column(String(60), ForeignKey('countries.id'), nullable=False)
        name = Column(String(128), nullable=False)
        matches = relationship("Match", backref="leagues")
    else:
        country_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """ Initialises League """
        super().__init__(*args, **kwargs)
