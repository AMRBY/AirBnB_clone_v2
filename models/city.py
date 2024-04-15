#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', cascade='all, delete', backref='city')
    else:
        name = ''
        state_id = ''

        @property
        def places(self):
            """ Getter method
            Returns a list of City instances with state_id == State.id
            """
            from models import storage

            places_list = []
            for val in storage.all(Place).values():
                if val.city_id == self.id:
                    places_list.append(val)

            return places_list
