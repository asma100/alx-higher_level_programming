#!/usr/bin/python3
"""task"""
from sqlalchemy.orm import relationship
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State, City


def create_california(username, password, db_name):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name='California')
    san_francisco = City(name='San Francisco')
    california.cities.append(san_francisco)

    session.add(california)
    session.commit()
    session.close()


if __name__ == "__main__":
    create_california(sys.argv[1], sys.argv[2], sys.argv[3])
