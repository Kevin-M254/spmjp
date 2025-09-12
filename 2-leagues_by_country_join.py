#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT leagues.id, leagues.name, countries.name
                FROM leagues
                JOIN countries
                ON leagues.country_id = countries.id
                ORDER BY leagues.id ASC""")
    [print(league) for league in cur.fetchall()]
