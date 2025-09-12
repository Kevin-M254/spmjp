#!/usr/bin/env
"""

"""
from sqlalchemy import Column, Integer, Float, String, ForeignKey, null
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Mjp(Base):
    """

    """
    __tablename__ = "mjp_2501-0106"
    id = Column(Integer, primary_key=True)
    match = Column(String(128), nullable=False)
    ht_odds = Column(Float, nullable=True)
    x_odds = Column(Float, nullable=True)
    at_odds = Column(Float, nullable=True)
    results = Column(String, nullable=True)
    league_id = Column(Integer, ForeignKey("leagues.id"), nullable=False)
