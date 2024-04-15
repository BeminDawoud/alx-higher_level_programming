#!/usr/bin/python3
"""
Comment
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
            f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{database}',
            pool_pre_ping=True)
    Base.metadata.create_all(engine)
    newState = State(name='Louisiana')

    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(newState)
    session.commit()

    print(newState.id)
