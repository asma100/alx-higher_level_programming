#!/usr/bin/python3
"""Defines  class """
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """ class  link  database"""
    __tablename__ = 'City'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer , foreign_key = states.id)

if __name__ == "__main__":
    from sqlalchemy import create_engine
    onnection_string = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(connection_string, pool_pre_ping=True)

    Base.metadata.create_all(engine)
