#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent the Airbnb User.

    Attributes:
        email (str): The user email.
        password (str): The user password.
        first_name (str): The user first_name.
        last_name (str): The user last_name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
