#!/usr/bin/python3
"""
Function to list all states from database
Database is an argument
"""
if __name__ == "__main__":

    import sys
    import MySQLdb

    # Arguments are assigned using index
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    query = "SELECT * FROM states ORDER BY states.id ASC"

    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        print(i)

    cursor.close()
    db.close()