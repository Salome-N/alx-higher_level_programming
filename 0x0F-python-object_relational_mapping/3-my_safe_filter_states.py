#!/usr/bin/python3
""" Takes in arguments and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
    But this time, write one that is safe from MySQL injections! """
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
    cursor.execute("SELECT * FROM states")
    states = cursor.fetchall()
    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
