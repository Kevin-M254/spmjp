#!/usr/bin/python3
""" Prediction class """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.sql.schema import ForeignKey
from os import getenv
import models


class Prediction(BaseModel, Base):
    """ Prediction attribute """
    if models.storage_t == "db":
        __tablename__ = "predictions"
        match_id = Column(String(60), ForeignKey("matches.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        prediction = Column(String(10), nullable=True)
