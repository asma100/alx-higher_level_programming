#!/usr/bin/python3
"""tasks"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a(username, password, db_name):
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(username, password, db_name), echo=False)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    username, password, db_name = sys.argv[1:]
    delete_states_with_a(username, password, db_name)
