#!/usr/bin/python3
"""DB Storage for sqlalchemy."""
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.user import User
from models.place import Place


class DBStorage:
    """ Database CRUD Operation"""
    __engine = None
    __session = None

    def __init__(self):
        env = getenv("HBNB_ENV")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """retrieve all objects of a given class from the
        database or, if no specific class is provided,
        retrieve all objects of certain predefined classes.
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)

    def new(self, obj):
        """Adds a new object to the current session
        """
        self.__session.add(obj)

    def save(self):
        """Commits changes to the database
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the database if provided
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """Configures the database connection and
        initializes the SQLAlchemy session
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """Closes the current session
        """
        self.__session.close()
