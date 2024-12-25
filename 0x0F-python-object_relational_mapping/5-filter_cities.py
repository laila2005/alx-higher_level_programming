#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
where the state name matches the argument passed.
Results are sorted by cities.id in asc order, and are
displayed as a comma-separated list.
"""
import MySQLdb
import sys

if __name__ == "__main__":

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()

    query = (
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.name ASC"
    )

    cur.execute(query, (sys.argv[4],))

    # Fetch all results
    rows = cur.fetchall()
    if rows:
        cities = ", ".join([row[0] for row in rows])
        print(cities)
    else:
        print(" ")

    # Close the cursor and database connection
    cur.close()
    db.close()
