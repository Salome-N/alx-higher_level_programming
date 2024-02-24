#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa by states """
import MySQLdb
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    host = 'localhost'
    port = 3306
    db = MySQLdb.connect(host, user, passwd, database, port)
    cursor = db.cursor()
    cursor.execute("SELECT c.id, c.name, s.name \
            FROM cities as c \
            INNER JOIN states as s \
            ON c.state_id = s.id \
            ORDER BY c.id")
    cities = cursor.fetchall()
    for city in cities:
        print(city)
