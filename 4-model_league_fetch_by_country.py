#!/usr/bin/python3
"""
Prints all League objects from spmjp
"""

import sys
from sqlalchemy import create_engine, true
from sqlalchemy.orm import sessionmaker
from model_country import Country
from model_league import League

if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    for league, country in session.query(League, Country)\
            .filter(League.country_id == Country.id)\
            .order_by(League.id):
                print("{}: ({}) {}".format(country.name, league.id, league.name))
