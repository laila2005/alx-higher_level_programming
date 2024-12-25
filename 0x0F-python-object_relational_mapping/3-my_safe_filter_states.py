#!/usr/bin/python3
"""
Script that takes in 4 arguments (MySQL username, password, database name, and state name)
and displays all states from the 'states' table where the name matches the argument.
Results are sorted by states.id in ascending order.
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
        "WHERE name = BINARY '{0}' "
        "ORDER BY id ASC"
    ).format(sys.argv[4])

    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
