#!/usr/bin/python3
"""lists all states with a name starting with N
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    DATABASE = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=USERNAME,
        passwd=PASSWORD,
        db=DATABASE,
        port=3306)

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        if row[1].startswith("N"):
            print(row)

    cur.close()
    db.close()
