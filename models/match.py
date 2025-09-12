#!/usr/bin/python3
""" Module for handling jackpot matches """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Table, ForeignKey
from os import getenv
import models


class Match(BaseModel, Base):
    """ Class for managing mjp objects
        Attributes:
            league_id (str): league id
            match_id (int): order of match in jp
            home_team (str): home team of match
            away_team (str): away team of match
            h_t_odds (float): home team odds
            x_odds (float): draw odds
            a_t_odds (float): away team odds
            results (str): results of match
            outcome (str): outcome of match
            h_t_pos (int): position of home team in table
            a_t_pos (int): position of away team 
            h_t_form (str): form of home team for last 6 matches
            h_t_win (int): home team wins
            a_t_win (int): away team wins
            h_t_draw (int): home team draws
            a_t_draw (int): away team draws
            h_t_lose (int): home team losses
            a_t_lose (int): away team losses
            h_t_win_percent (int): win percentage
            a_t_win_percent (int): win percentage
    """
    __tablename__ = "matches"
    if models.storage_t == "db":
        league_id = Column(String(60), ForeignKey("leagues.id"), nullable=False)
        match_id = Column(Integer, nullable=False)
        home_team = Column(String(60), nullable=False)
        away_team = Column(String(60), nullable=False)
        h_t_odds = Column(Float, nullable=False)
        x_odds = Column(Float, nullable=False)
        a_t_odds = Column(Float, nullable=False)
        h_t_pos = Column(Integer, nullable=False, default=0)
        a_t_pos = Column(Integer, nullable=False, default=0)
        h_t_form = Column(String(10), nullable=True)
        a_t_form = Column(String(10), nullable=True)
        h_t_win = Column(Integer, nullable=False, default=0)
        a_t_win = Column(Integer, nullable=False, default=0)
        h_t_draw = Column(Integer, nullable=False, default=0)
        a_t_draw = Column(Integer, nullable=False, default=0)
        h_t_lose = Column(Integer, nullable=False, default=0)
        a_t_lose = Column(Integer, nullable=False, default=0)
        h_t_win_percent = Column(Integer, nullable=False, default=0)
        a_t_win_percent = Column(Integer, nullable=False, default=0)
        results = Column(String(10), nullable=True)
        outcome = Column(String(10), nullable=True)
        prediction = relationship("Prediction", backref="match",
                                  cascade="all, delete, delete-orphan")
        #teams = relationship("Team", secondary="match_data",
                             #backref="matches_data", viewonly=False)

    else:
        league_id = ""
        match_id =0
        home_team = ""
        away_team = ""
        h_t_odds = 0.0
        x_odds = 0.0
        a_t_odds = 0.0
        h_t_pos = 0
        a_t_pos = 0
        h_t_win = 0
        a_t_win = 0
        h_t_draw = 0
        a_t_draw = 0
        h_t_lose = 0
        a_t_lose = 0
        h_t_form = ""
        a_t_form = ""
        h_t_win_percent = 0
        a_t_win_percent = 0
        results = ""
        outcome = ""

        @property
        def prediction(self):
            """ Getter attribute reviews that returns list of all
              Prediction instances with match_id equals to current
              Match.id
            """
            from models.prediction import Prediction
            prediction = []
            for prediction in storage.all(Prediction).values():
                if prediction.match_id == self.id:
                    prediction.append(prediction)
            return prediction
