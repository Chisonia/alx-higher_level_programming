#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    import MySQLdb 

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],  # Use 'passwd' instead of 'password'
        db=sys.argv[3]  # Use 'db' instead of 'db_name'
    )

    query = "SELECT * FROM states ORDER BY states.id ASC"

    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    for item in result:
        print(item)
    
    cursor.close()
    db.close()