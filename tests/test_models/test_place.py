#!/usr/bin/python3
"""Unittest module for the Place Class."""

import unittest
from datetime import datetime
import time
from models.place import Place
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
from tests.test_models.test_base_model import TestBaseModel


class TestPlace(TestBaseModel):

    """Test Cases for the Place class."""

    def setUp(self):
        """Sets up test methods."""
        self.name = "Place"
        self.value = Place

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests instantiation of Place class."""

        b = Place()
        self.assertEqual(str(type(b)), "<class 'models.place.Place'>")
        self.assertIsInstance(b, Place)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "city_id"))
        self.assertEqual(new.city_id, "")

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "user_id"))
        self.assertEqual(new.user_id, "")

    def test_name4(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "name"))
        self.assertEqual(new.name, "")

    def test_description(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "description"))
        self.assertEqual(new.description, "")

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "number_rooms"))
        self.assertEqual(new.number_rooms, 0)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "number_bathrooms"))
        self.assertEqual(new.number_bathrooms, 0)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "max_guest"))
        self.assertEqual(new.max_guest, 0)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "price_by_night"))
        self.assertEqual(new.price_by_night, 0)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "latitude"))
        self.assertEqual(new.latitude, 0.0)
