#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel
from models import storage
from models.city import City

class State(BaseModel, Base):
    """Represent the Airbnb state.

    Attributes:
        name (str): The name of the Airbnb state.
    """
    __tablename__ = "states"

    name = column(string(128), nullable=False)

    if environ.get('HBNB_TYPE_STORAGE') == "db":
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        @property
        def cities(self):
            """Getter method for cities"""

            # return list of City objs in __objects
            cities_dict = storage.all(City)
            cities_list = []

            # copy values from dict to list
            for city in cities_dict.values():
                if city.state_id == self.id:
                    cities_list.append(city)

            return cities_list
