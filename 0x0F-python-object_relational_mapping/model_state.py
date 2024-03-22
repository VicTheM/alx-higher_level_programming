#!/usr/bin/python3
"""contains the class definition of a State"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    """Represents a table of states"""
    __tablename__ = "states"
    id = Column(
            Integer,
            autoincrement=True,
            nullable=False,
            unique=True,
            primary_key=True)
    name = Column(String(128), nullable=False)
