#!/usr/bin/python3
""" lists all states with a name starting with N 
    from the database hbtn_0e_0_usa """
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
    cursor.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in cursor.fetchall() if state[1][0] == "N"]
