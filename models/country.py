#!/usr/bin/python3
""" Module for Country class """
from models.base_model import BaseModel, Base
from models import storage_t
from models.league import League
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Country(BaseModel, Base):
    """ Class to manage country objects 
        Attributes:
            name (str): name of country
    """
    __tablename__ = 'countries'
    if storage_t == 'db':
        name = Column(String(128), nullable=False)
        leagues = relationship('League', backref='country',
                               cascade='all, delete, delete-orphan')
    else:
        name = ""

        @property
        def leagues(self):
            ''' Returns a list of League instances with country_id
                equals to the current Country.id
            '''
            from models import storage
            related_leagues = []
            leagues = storage.all(League)
            for league in leagues.values():
                if league.country_id == self.id:
                    related_leagues.append(league)
            return related_leagues

    def __init__(self, *args, **kwargs):
        """ Initialise Country """
        super().__init__(*args, **kwargs)
