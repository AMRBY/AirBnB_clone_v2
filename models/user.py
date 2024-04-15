#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship('Place', cascade='all, delete', backref='user')
        reviews = relationship('Review', cascade='all, delete', backref='review')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
        @property
        def places(self):
            """ Getter method
            Returns a list of City instances with state_id == State.id
            """
            from models import storage

            places_list = []
            for val in storage.all(Place).values():
                if val.user_id == self.id:
                    places_list.append(val)

            return places_list
        @property
        def reviews(self):
            """ Getter method
            Returns a list of City instances with state_id == State.id
            """
            from models import storage

            reviews_list = []
            for val in storage.all(Review).values():
                if val.user_id == self.id:
                    reviews_list.append(val)

            return places_list
