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
    arg = sys.argv[4]

    engine = create_engine(
            f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{database}',
            pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State).filter(State.name == arg).first()
    print(f"{res.id}" if res else "Not found")
