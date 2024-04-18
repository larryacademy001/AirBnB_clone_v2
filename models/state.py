#!/usr/bin/python3
"""
State Module - Contains the State class
"""
import models
from models.city import City
import shlex
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String


class State(BaseModel, Base):
    """
    State class inherits from BaseModel and represents state

    Public class attribute
        name (str): The name of the state.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        query_result = models.storage.all()
        my_list = []
        my_result = []
        for key in query_result:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                my_list.append(query_result[key])
        for elem in my_list:
            if (elem.state_id == self.id):
                my_result.append(elem)
        return (my_result)
