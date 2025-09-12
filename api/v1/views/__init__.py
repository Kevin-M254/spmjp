#!/usr/bin/python3
""" API blueprint """
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


from api.v1.views.index import *
from api.v1.views.countries import *
from api.v1.views.leagues import *
from api.v1.views.matches import *
from api.v1.views.users import *
from api.v1.views.predictions import *
