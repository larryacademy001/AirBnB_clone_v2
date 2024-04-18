#!/usr/bin/python3
"""City class with SQLAlchemy ORM mappings, including
relationships with other classes such as Place
"""
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    City class inherits from BaseModel and represents a city

    Public class attributes
        state_id (str): The ID of the state the city belongs to.
        name (str): The name of the city.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
