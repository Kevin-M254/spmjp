#!/usr/bin/python3
"""
  Print Country object of country passed as state
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_country import Base, Country

if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    for country in session.query(Country):
        if sys.argv[4] == country.name:
            print("{}".format(country.id))
            break
    else:
        print("Not found")
