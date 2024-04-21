#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    """amenity class with Many to Many"""
    if getenv("HBNB_TYPE_STORAGE") == "db": 
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        # place_amenities = relationship("Place", secondary="place_amenity", viewonly=False, back_populates="amenities")
    else:
        name = ""
