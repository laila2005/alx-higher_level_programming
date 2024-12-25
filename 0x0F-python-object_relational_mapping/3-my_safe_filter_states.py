#!/usr/bin/python3
"""
Script that takes in 4 arguments
and displays all states from the 'states'
table where the name matches the argument.
Results are sorted by states.id in asc order.
"""
import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()

    query = (
        "SELECT id, name FROM states "
        "WHERE name = BINARY %s "
        "ORDER BY id ASC"
    )

    cur.execute(query, (sys.argv[4],))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
