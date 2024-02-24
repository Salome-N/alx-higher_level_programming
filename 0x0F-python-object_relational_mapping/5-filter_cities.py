#!/usr/bin/python3
""" takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_4_usa """
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
    print(", ".join([city[1]for city in cities if city[2] == sys.argv[4]]))
