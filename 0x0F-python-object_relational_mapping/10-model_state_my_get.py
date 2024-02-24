#!/usr/bin/python3
""" prints the State object with the name passed as
    argument from the database hbtn_0e_6_usa """
import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    uri_db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
             sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(uri_db, pool_pre_ping=True)
    Session = Session(bind=engine)
    found = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = True
            break
    if found is False:
        print("Not found")
    session.close()
