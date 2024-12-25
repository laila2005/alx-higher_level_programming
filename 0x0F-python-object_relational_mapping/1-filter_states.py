#!/usr/bin/python3
"""
Module that lists all states from the database hbtn_0e_0_usa.
that starts with N
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
    cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(f"({row[0]}, '{row[1]}')")
    cur.close()
    db.close()
