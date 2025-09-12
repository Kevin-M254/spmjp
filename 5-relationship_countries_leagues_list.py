#!/usr/bin/python3
"""
  Lists all countries and corresponding leagues in spmjp
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_country import Country
from relationship_league import League

if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    for country in session.query(Country).order_by(Country.id):
        print("{}: {}".format(country.id, country.name))
        for league in country.leagues:
            print("     {}: {}".format(league.id, league.name))
