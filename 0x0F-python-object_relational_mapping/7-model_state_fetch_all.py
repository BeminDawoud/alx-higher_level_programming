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
    
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(user, pwd, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for res in session.query(State):
        print(f"{res.id}: {res.name}")
