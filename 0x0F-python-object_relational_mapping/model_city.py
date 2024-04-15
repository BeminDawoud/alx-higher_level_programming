#!/usr/bin/python3
"""
comment
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):

    """Class of City"""

    __tablename__ = 'cities'

    id = Column(
            Integer,
            autoincrement=True,
            nullable=False,
            primary_key=True
            )
    name = Column(
            String(128),
            nullable=False
            )
    state_id = Column(
            Integer,
            ForeignKey('states.id'),
            nullable=False)
