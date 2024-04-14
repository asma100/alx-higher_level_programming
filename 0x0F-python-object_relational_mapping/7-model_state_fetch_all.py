#!/usr/bin/python3
"""task"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State
import sys 

def list_objects(username, password, db_name):
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{db_name}', pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))


if __name__ == "__main__":
    list_objects(sys.argv[1], sys.argv[2], sys.argv[3])
