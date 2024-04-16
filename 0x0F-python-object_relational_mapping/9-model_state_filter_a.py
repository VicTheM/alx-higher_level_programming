#!/usr/bin/python3
"""This script lists all State objects that contain the
letter a from the database hbtn_0e_6_usa"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    db = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3])
    engine = create_engine(db, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    query = session.query(State).filter(State.name.like("%a%"))
    for state in query.order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    session.close()
