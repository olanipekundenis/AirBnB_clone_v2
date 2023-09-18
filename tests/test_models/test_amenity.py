#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
from datetime import datetime
import time
from models.amenity import Amenity
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
from tests.test_models.test_base_model import TestBaseModel


class TestAmenity(TestBaseModel):

    """Test Cases for the Amenity class."""

    def setUp(self):
        """Sets up test methods."""
        self.name = "Amenity"
        self.value = Amenity

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
        """Tests instantiation of Amenity class."""

        b = Amenity()
        self.assertEqual(str(type(b)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(b, Amenity)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_name2(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "name"))
        self.assertEqual(new.name, "")


if __name__ == "__main__":
    unittest.main()
