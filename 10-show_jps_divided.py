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

    #num = 17, 34, 51, 68, 85, 102, 119, 136, 151, 168, 185, 
    for match in session.query(Mjp).order_by(Mjp.id):
        #num = [318, 301]
        if match.id == 369:
            print("\n")
        elif match.id == 352:
            print("\n")
        elif match.id == 335:
            print("\n")
        elif match.id == 318:
            #match.id += 17
            print("\n")
        elif match.id == 301:
            print("\n")
        elif match.id == 284:
            print('\n')
        elif match.id == 267:
            print('\n')
        elif match.id == 250:
            print('\n')
        elif match.id == 233:
            print('\n')
        print("{}	| {}  {}  {} |	({})".format(match.match, match.ht_odds, match.x_odds,match.at_odds, match.results))
