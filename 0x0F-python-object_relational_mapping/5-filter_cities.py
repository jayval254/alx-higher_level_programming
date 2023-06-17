#!/usr/bin/python3
""" lists all cities of a state
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    DATABASE = sys.argv[3]
    searched = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=USERNAME,
        passwd=PASSWORD,
        db=DATABASE,
        port=3306)

    cur = db.cursor()

    cur.execute("SELECT cities.name, states.name \
                FROM cities INNER JOIN states on cities.state_id = states.id\
                ORDER BY cities.id ASC")
    rows = cur.fetchall()

    list = []

    for row in rows:
        if row[1] == searched:
            list.append(row[0])

    output = ", ".join(list)
    print(output)

    cur.close()
    db.close()
