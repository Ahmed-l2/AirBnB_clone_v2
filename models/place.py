#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Float, Integer, Table
from models import storage_type
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity


if storage_type == "db":
    place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id",
                                 String(60)
                                 ForeignKey('places.id')
                                 primary_key=True
                                 nullable=False)
                          Column("amenity_id",
                                 String(60)
                                 ForeignKey("amenities.id")
                                 primary_key=True
                                 nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if storage_type == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place', cascade='all,\
                              delete, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False, backref='place_amenities')

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """getter for list of city instances related to the state"""
            from models import storage
            related_reviews = []
            reviews = storage.all(Review)
            for review in reviews.values():
                if review.place_id == self.id:
                    related_reviews.append(review)
            return related_reviews

        @property
        def amenities(self):
            """getter for list of amenity instances related to the place"""
            from models import storage
            related_amenities = []
            amenities = storage.all(Amenity)
            for amenity in amenities.values():
                if amenity.place_id == self.id:
                    related_amenities.append(amenity)
            return related_amenities

        @amenities.setter
        def amenities(self, obj):
            """setter for list of amenity instances related to the place"""
            if obj:
                if isinstance(obj, Amenity):
                    if obj.id not in self.amenity_ids:
                        self.amenity_ids.append(obj.id)
