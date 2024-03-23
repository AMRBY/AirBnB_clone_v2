#!/usr/bin/python3
"""This module defines a class to manage DB storage for hbnb clone"""
from os import getenv
from models import Base, User, State, City, Amenity, Place, Review 


class DBStrogae(Base):
    """This class should manage the db storage
    """
    __engine = None
    __session = None
    __classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place, 'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}

    def __init__(self):
        """initialization of the class DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                .format(getenv('HBNB_MYSQL_USER'), 
                    getenv('HBNB_MYSQL_PWD'), getenv('HBNB_MYSQL_HOST'), 
                    getenv('HBNB_MYSQL_DB'), pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """show all queries"""
        dictionnary = {}
        self.__session = Session(self.__engine)
        if cls:
            for row_data in self.__session.query(cls).all():
                key = self.__class__.__name__ + '.' + self.id
                dictionnary[key] = row_data
        else:
            #for k, v in self.__classes.items():
            for row_data in self.__session.query().all():
                key = self.__class__.__name__ + '.' + self.id
                dictionnary[key] = row_data

        return dictionnary

    def new(self, obj):
        """add a new object to DB"""
        self.__session.add(obj)

    def save(self):
        """save an object to DB"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete an obj from DB"""
        if obj is not None: 
            self.__session.delete(obj)

    def reload(self):
        """reload all data from DB"""
        from sqlalchemy.orm import scoped_session
        from sqlalchemy.orm import sessionmaker
        Base.metadata.create_all(self.__engine)
        ses = sessionmaker(self.__engine, expire_on_commit=False) 
        self.__session = scoped_session(ses)
