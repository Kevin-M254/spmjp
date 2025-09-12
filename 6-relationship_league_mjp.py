#!/usr/bin/python3
"""
"""

import sys
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from relationship_league import League
from relationship_mjp import Mjp

if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    for league in session.query(League).order_by(desc(League.id)).all():
        print("{}".format(league.name))
        for mjp in league.mjp:
            print(" {}  ({}  {}  {}) - {}".format(mjp.match, mjp.ht_odds,
                                           mjp.x_odds, mjp.at_odds,
                                           mjp.results))
