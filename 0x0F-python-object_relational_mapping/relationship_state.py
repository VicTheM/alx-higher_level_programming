#!/usr/bin/python3
"""contains the class definition of a State"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

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
    cities = relationship(
            "City",
            backref="state",
            cascade="all, delete-orphan",
            order_by="City.id"
            )
