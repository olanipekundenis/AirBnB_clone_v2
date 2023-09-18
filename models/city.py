#!/usr/bin/python3
"""Defines City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent the Airbnb city.

    Attributes:
        state_id (str): The Airbnb state id.
        name (str): The name of the Airbnb city.
    """

    state_id = ""
    name = ""
