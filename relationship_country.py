#!/usr/bin/python3
"""
  Defines a country model that contains class definition of Country
  and an instance Base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_league import Base, League


class Country(Base):
    """ 
      Attributes:
        id, name.
    """
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    leagues = relationship("League", backref="country", cascade="all, delete")
