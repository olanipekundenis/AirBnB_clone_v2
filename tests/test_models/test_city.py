#!/usr/bin/python3
"""Unittest module for the City Class."""

import unittest
from datetime import datetime
import time
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
from tests.test_models.test_base_model import TestBaseModel


class TestCity(TestBaseModel):

    """Test Cases for the City class."""

    def setUp(self):
        """Sets up test methods."""
        self.name = "City"
        self.value = City

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
        """Tests instantiation of City class."""

        b = City()
        self.assertEqual(str(type(b)), "<class 'models.city.City'>")
        self.assertIsInstance(b, City)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "state_id"))
        self.assertEqual(new.state_id, "")

    def test_name3(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "name"))
        self.assertEqual(new.name, "")


if __name__ == "__main__":
    unittest.main()
