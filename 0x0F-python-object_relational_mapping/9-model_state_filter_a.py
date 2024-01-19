#!/usr/bin/python3
"""
Lists all State objects with the letter 'a' from database
"""

from sys import argv
import MySQLdb
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        for c in state.name:
            if c == 'a':
                print("{}: {}".format(state.id, state.name))
                break
    session.close()
