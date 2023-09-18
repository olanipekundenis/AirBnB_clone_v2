#!/usr/bin/python3
"""Defines the Amenity on the Airbnb"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Blueprint of an amenity.

    Attributes:
        name (str): name of the amenity.
    """

    name = ""
