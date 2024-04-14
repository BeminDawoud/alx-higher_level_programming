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
            "SELECT cities.name FROM cities "
            "INNER JOIN states ON states.id = cities.state_id "
            "WHERE states.name = %s ORDER BY cities.id ASC", (arg,)
            )
    results = list(cur.fetchall())
    print(", ".join([res[0] for res in results]))
    cur.close()
    db.close()
