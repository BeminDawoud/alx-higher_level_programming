#!/usr/bin/python3
"""
0-select_states.py
"""

import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=user,
            passwd=pwd,
            db=database
            )
    cur = db.cursor()
    cur.execute(
            "SELECT * FROM cities "
            "ORDER BY cities.id ASC"
            )
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
