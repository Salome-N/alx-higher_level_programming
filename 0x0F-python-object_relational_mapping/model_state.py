#!/usr/bin/python3
""" class definition of a State """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ Represents State from MySQL database.

    __tablename__(str): name of the MySQL table to store States.
    id (sqlalchamey.Integer): State id
    name (sqlalchemy.String): State name
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True,
                unique=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
