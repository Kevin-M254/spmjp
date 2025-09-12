#!/usr/bin/python3
"""
    Lists all leagues of country passed as argument
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM leagues
                INNER JOIN countries
                ON leagues.country_id = countries.id
                ORDER BY leagues.id""")
    print("\n".join([league[2]
                     for league in c.fetchall()
                     if league[4] == sys.argv[4]]))
