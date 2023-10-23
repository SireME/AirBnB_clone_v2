#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship as rl
import os


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(60), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        state = rl("State", back_populates="cities")
        places = rl("Place", back_populates="cities", cascade="all, delete")
    else:
        name = ""
        state_id = ""
