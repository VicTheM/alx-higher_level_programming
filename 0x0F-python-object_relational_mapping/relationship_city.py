#!/usr/bin/python3
"""contains the class definition of a State"""
from relationship_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """Represents a table of cities"""
    __tablename__ = "cities"
    id = Column(
            Integer,
            autoincrement=True,
            nullable=False,
            unique=True,
            primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
