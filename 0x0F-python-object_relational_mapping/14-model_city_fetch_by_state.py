#!/usr/bin/python3
""" prints all City objects from the database hbtn_0e_14_usa """
import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    uri_db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
             sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(uri_db, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State, City).filter(State.id == City.state_id).all()
    for state, city in query:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.close()
