#!/usr/bin/python3
""" State class """
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Represents State from MySQL database.

    __tablename__(str): name of the MySQL table to store States.
    id (sqlalchamey.Integer): State id
    name (sqlalchemy.String): State name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                unique=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City',
                          cascade='all, delete-orphan',
                          backref=backref("state", cascade="all"))
