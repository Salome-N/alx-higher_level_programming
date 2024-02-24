#!/usr/bin/python3
""" changes the name of a State object from the database hbtn_0e_6_usa """
import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError


if __name__ == "__main__":
    uri_db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
             sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(uri_db, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        result = session.query(State).filter(State.id == 2).first()
        result.name = "New Mexico"
        session.commit()
    except SQLAlchemyError as error:
        pass
    finally:
        session.close()
