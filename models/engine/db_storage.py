#!/usr/bin/python3
"""This is the file storage class for AirBnB"""

from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place

from sqlalchemy import (create_engine)
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from os import environ

class DBStorage:
    """ Storage for database"""
    __engine = None
    __session = None

    def __init__(self):
        """constructor"""
        MySqlUser = environ.get('HBNB_MYSQL_USER')
        MySqlPwd = environ.get('HBNB_MYSQL_PWD')
        MySqlHost = environ.get('HBNB_MYSQL_HOST')
        MySqlDb = environ.get('HBNB_MYSQL_DB')
        MySqlEnv = environ.get('HBNB_ENV')

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(MySqlUser, MySqlPwd, MySqlHost,
                                          MySqlDb), pool_pre_ping=True)
        if MySqlEnv == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''uery on the current database session (self.__session)
        all objects depending of the class name (argument cls)'''
        
        dct = {}
        if not cls:
            tables = [User, State, City, Place]
            for table in tables:
                query = self.__session.query(table).all()

                for obj in query:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    dct[key] = obj
        else:
            query = self.__session.query(cls).all()
            for obj in query:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                dct[key] = obj
        return dct

    def new(self, obj):
        """ add the object to the current database session """
        if obj:
            self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from module import symbol
        the current database session obj if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        creates all tables in the database
        creates the current database session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Close Session
        """
        self.__session.close()
