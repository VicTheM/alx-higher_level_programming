#!/usr/bin/python3
"""This script prints all City objects from the database hbtn_0e_14_usa"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    db = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3])
    engine = create_engine(db, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    query = session.query(
            State.name,
            City.id,
            City.name
            ).join(State)
    for city in query.all():
        print("{0}: ({1}) {2}".format(*city))

    session.close()
