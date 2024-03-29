#!/usr/bin/python3
""" Creates the State “California” with the City “San Francisco” """
import sys
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import Session
from relationship_city import City
from relationship_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
    session.close()
