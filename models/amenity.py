#!/usr/bin/python3
"""Amenity class with SQLAlchemy ORM mappings
including a relationship with the Place class
to represent the many-to-many relationship
between amenities and places.

"""
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """
    Amenity class inherits from BaseModel and represents an amenity

    Public class attributes:
        name (str): The name of the amenity.

    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
