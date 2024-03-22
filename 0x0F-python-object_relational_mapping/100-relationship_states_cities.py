#!/usr/bin/python3
"""This script creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa:"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    db = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3])
    engine = create_engine(db, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    state = State(name="California")
    city = City(name="San Francisco", state=state)
    session.add(state)
    session.commit()

    session.close()
