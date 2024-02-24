#!/usr/bin/python3
""" adds the State object “Louisiana” to the database hbtn_0e_6_usa """
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
    new_state = State(name='Louisiana')
    query = session.add(new_state)
    session.commit()
    louisiana = session.query(State).filter(State.name == 'Louisiana').first()
    print(louisiana.id)
    session.close()
