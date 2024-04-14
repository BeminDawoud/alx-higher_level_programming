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
    arg = sys.argv[4]

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=user,
            passwd=pwd,
            db=database
            )
    cur = db.cursor()
    cur.execute(
            "SELECT * FROM states WHERE BINARY name = '{}'"
            "ORDER BY states.id ASC".format(arg)
            )
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
