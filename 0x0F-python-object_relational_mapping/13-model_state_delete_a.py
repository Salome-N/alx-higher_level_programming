#!/usr/bin/python3
""" deletes all State objects with a name containing
    the letter a from the database hbtn_0e_6_usa """
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
    results = session.query(State).filter(State.name.like('%a%')).all()
    for state in results:
        session.delete(state)
    session.commit()
    session.close()
