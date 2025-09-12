#!/usr/bin/python3
"""
  Defines a country model that contains class definition of Country
  and an instance Base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Country(Base):
    """ 
      Attributes:
        id, name.
    """
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
