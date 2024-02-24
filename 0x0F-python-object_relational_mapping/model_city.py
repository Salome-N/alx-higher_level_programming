#!/usr/bin/python3
""" City Class """
from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base


class City(Base):
    """ Represents city """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
         unique=True, autoincrement=True,
         nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'),
                      nullable=False)
