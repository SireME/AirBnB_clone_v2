#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb
using a database clone
"""


class DBStorage:
    """This class manages storage of hbnb models in database"""
    __engine = None
    __session = None

    def __init__(self):
        from os import getenv
        from sqlalchemy import create_engine, MetaData

        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        dbe = f"mysql+mysqldb://{user}:{pwd}@{host}/{db}"
        self.__engine = create_engine(dbe, pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            metadata = MetaData()
            metadata.bind = engine
            metadata.drop_all(engine)

    def all(self, cls=None):
        """Returns a dict of specific/all models currently in storage"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        session = self.__session
        obj = {}
        if cls:
            to_query = [cls]
        else:
            to_query = [User, State, City, Amenity, Place, Review]
        for cls_obj in to_query:
            result = session.query(cls_obj).all()
            for q_obj in result:
                key = cls_obj.__name__ + "." + q_obj.id
                obj[key] = q_obj
        return obj

    def new(self, obj):
        """Adds new object to current database session"""
        session = self.__session
        session.add(obj)

    def save(self):
        """Permanently commit all changes to db session storage"""
        session = self.__session
        session.commit()

    def delete(self, obj=None):
        """
        instance method to delete object from current db session
        """
        if obj:
            session = self.__session
            session.delete(obj)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from sqlalchemy.orm import sessionmaker, scoped_session
        from models.base_model import Base

        engine = self.__engine
        Session = sessionmaker(bind=engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

        Base.metadata.create_all(engine)
