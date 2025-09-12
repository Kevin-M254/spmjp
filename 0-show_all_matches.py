#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM `mjp-25-01-25`""")
    rows = cur.fetchall()

    for row in rows:
        print(row)
