#!/usr/bin/python3
"""
Module that lists all cities from the database hbtn_0e_4_usa
where the state name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    
    # Create cursor
    cur = db.cursor()

    # Use parameterized query to avoid SQL injection
    query = """
    SELECT cities.name 
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """
    
    # Execute query with the state name argument
    cur.execute(query, (sys.argv[4],))

    # Fetch all rows
    rows = cur.fetchall()

    # Print cities or a message if no cities are found
    if rows:
        print(", ".join([row[0] for row in rows]))
    else:
        print(" ")

    # Close the cursor and the database connection
    cur.close()
    db.close()
