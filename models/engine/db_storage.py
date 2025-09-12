#!/usr/bin/python3
""" Database storage engine """
from os import getenv
from models.base_model import BaseModel, Base
import models
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import text
from models.country import Country
from models.league import League
from models.match import Match
from models.user import User
from models.prediction import Prediction

classes = {"Country": Country, "League": League, "Match": Match,
           "User": User, "Prediction": Prediction}


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        SPMJP_USER = getenv('SPMJP_USER')
        SPMJP_PWD = getenv('SPMJP_PWD')
        SPMJP_HOST = getenv('SPMJP_HOST', default='localhost')
        SPMJP_DB = getenv('SPMJP_DB')
        SPMJP_ENV = getenv('SPMJP_ENV')

        self.__engine = create_engine(
                'mysql+mysqldb://' +
                SPMJP_USER +
                ':' +
                SPMJP_PWD +
                '@' +
                SPMJP_HOST +
                '/' +
                SPMJP_DB)

        if SPMJP_ENV == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        objects = {}
        for val in classes:
            if cls is None or cls is classes[val] or cls is val:
                objs = self.__session.query(classes[val]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    objects[key] = obj
            
        return (objects)

    def new(self, obj):
        ''' Adds object to current database session '''
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as ex:
                self.__session.rollback()
                raise ex

    def save(self):
        """ Commit all changes to current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from current database session obj if not None """
        if obj is not None:
            self.__session.query(type(obj)).filter(
                    type(obj).id == obj.id).delete()

    def reload(self):
        ''' Creates all tables in the database '''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

    def get(self, cls, id):
        """ Returns object based on the class name and id, 
          None if not found """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """ Count number of objects in storage """
        clss = classes.values()

        if not cls:
            count = 0
            for val in clss:
                count += len(models.storage.all(val).values())
        else:
            count = len(models.storage.all(cls).values())
            
        return count

    def close(self):
        """ Closes the working database session """
        self.__session.close()
