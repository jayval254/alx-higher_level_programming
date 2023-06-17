#!/usr/bin/python3
"""
State class
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from model_state import Base, State


class City(Base):
    """City Class

    Attributes:
    id, name, state_id
    """
    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer,
                      ForeignKey('states.id'), nullable=False)
