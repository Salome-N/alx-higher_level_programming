#!/usr/bin/python3
""" takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument. """
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
    cursor.execute("SELECT * \
            FROM `states` \
            WHERE BINARY `name` = '{}'".format(sys.argv[4]))
    states = cursor.fetchall()
    for state in states:
        print(state)
