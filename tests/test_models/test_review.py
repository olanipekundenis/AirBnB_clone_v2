#!/usr/bin/python3
"""Unittest module for the Review Class."""

import unittest
from datetime import datetime
import time
from models.review import Review
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
from tests.test_models.test_base_model import TestBaseModel


class TestReview(TestBaseModel):

    """Test Cases for the Review class."""

    def setUp(self):
        """Sets up test methods."""
        self.name = "Review"
        self.value = Review

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
        """Tests instantiation of Review class."""

        b = Review()
        self.assertEqual(str(type(b)), "<class 'models.review.Review'>")
        self.assertIsInstance(b, Review)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "place_id"))
        self.assertEqual(new.place_id, "")

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "user_id"))
        self.assertEqual(new.user_id, "")
       

    def test_text(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "text"))
        self.assertEqual(new.text, "")



if __name__ == "__main__":
    unittest.main()
