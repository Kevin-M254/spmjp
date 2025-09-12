#!/usr/bin/python3
"""
  Defines a League model that contains class definition of leagues
  and instance Base
"""
from relationship_mjp import Base, Mjp
from unicodedata import name
from sqlalchemy import Column, Integer, String, ForeignKey, null
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class League(Base):
    
    __tablename__ = "leagues"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    country_id = Column(Integer, ForeignKey("countries.id"), nullable=False)

    mjp = relationship("Mjp", backref="league", cascade="all, delete")
