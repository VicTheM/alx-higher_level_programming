#!/usr/bin/python3
"""This script lists all City objects from the database hbtn_0e_101_usa"""
from sys import argv
from relationship_state import Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    db = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3])
    engine = create_engine(db, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    query = session.query(City).order_by(City.id)

    for city in query.all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
