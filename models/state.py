#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship as rl
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        cities = rl(
                "City",
                back_populates="state",
                cascade='all, delete'
                )
    else:
        @property
        def cities(self):
            "return all cities in the state"
            from models import storage
            cities_state = []
            for value in storage.all(City).values():
                if value.state_id == self.id:
                    cities_state.append(value)
            return cities_state
