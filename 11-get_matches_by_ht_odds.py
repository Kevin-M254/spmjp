#!/usr/bin/python3
"""
"""

import sys
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from relationship_country import Country
from relationship_league import League
from relationship_mjp import Mjp

if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    for match in session.query(Mjp):
        match.ht_odds = 0.0
        if match.ht_odds <= float(sys.argv[4]) is True:
            print("{}  | {} {} {} | ({})".format(match.match, match.ht_odds, match.x_odds, match.at_odds, match.results))
