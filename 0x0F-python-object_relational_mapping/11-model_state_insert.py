#!/usr/bin/python3
"""
Adds an object to database
"""

from sys import argv
import MySQLdb
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import update

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    new = State(name="Louisiana")
    session.add(new)
    session.commit()
    for state in session.query(State).filter_by(name="Louisiana")\
                                     .order_by(State.id).all():
        print("{}".format(state.id))
    session.close()
