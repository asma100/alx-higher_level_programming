#!/usr/bin/python3
"""task"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys


def print_first_state(username, password, db_name):
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).order_by(State.id).all()
    if not states_with_a:
        print("Nothing")
    else:
        for state in states_with_a:
            if "a" in state.name:
                print("{}: {}".format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    print_first_state(sys.argv[1], sys.argv[2], sys.argv[3])
