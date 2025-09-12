#!/usr/bin/python3
"""
  Defines a League model that contains class definition of leagues
  and instance Base
"""
import models
from models.base_model import BaseModel, Base
from unicodedata import name
from os import getenv
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, null
from sqlalchemy.orm import relationship


class League(BaseModel, Base):
    """ Representation of a league """
    if models.storage_t == "db":
        __tablename__ = "leagues"
        id = Column(Integer, primary_key=True)
        name = Column(String(128), nullable=False)
        country_id = Column(Integer, ForeignKey("countries.id"), nullable=False)
