#!/usr/bin/python3
""" Serializes instances to a json file and
    deserialises json file to instances
"""
from models.base_model import BaseModel
from models.user import User
from models.country import Country
from models.league import League
from models.match import Match
#from models.team import Team
from models.prediction import Prediction
import os.path
import json
import models

classes = {"Country": Country, "League": League, "Match": Match,
           "User": User, "Prediction": Prediction}


class FileStorage:
    """ Represents an abstract storage engine
        Attributes:
            __file_path (str): name of file to save objects
            __objects (dict) : a dictionary of instatiated objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """ Returns the dictionary __objects """
        if cls is None:
            return FileStorage.__objects
        else:
            obj_dict = {}
            for key, value in FileStorage.__objects.items():
                if isinstance(value, cls):
                    obj_dict[key] = value
            return obj_dict

    def new(self, obj):
        """ Sets obj with key <obj_class_name> """
        obj_cls_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_cls_name,
                                             obj.id)] = obj

    def save(self):
        """ Serialises __objects to JSON file __file_path """
        o_dict = FileStorage.__objects
        obj_dict = {obj: o_dict[obj].to_dict() for obj in o_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """ Desrialises JSON file to __objects """
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for i in obj_dict.values():
                    cls_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(cls_name)(**i))
        except FileNotFoundError:
            return

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

    def delete(self, obj=None):
        """ Delete obj from __objects """
        if obj is not None:
            key = obj.__class__.__name__+'.'+obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        self.reload()
