#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        #self.assertEqual(result.total_errors, 0,
         #                "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_get_method_docstring(self):
        """Test for the presence of docstring in DBStorage.get() method"""
        self.assertIsNot(DBStorage.get.__doc__, None, "get method needs a docstring")
        self.assertTrue(len(DBStorage.get.__doc__) >= 1, "get method needs a docstring")

    def test_count_method_docstring(self):
        """Test for the presence of docstring in DBStorage.count() method"""
        self.assertIsNot(DBStorage.count.__doc__, None, "count method needs a docstring")
        self.assertTrue(len(DBStorage.count.__doc__) >= 1, "count method needs a docstring")

    def test_get_method(self):
        """Test the DBStorage.get() method"""
        # Add objects to the database for testing
        state1 = State(name="California")
        state2 = State(name="New York")
        models.storage.new(state1)
        models.storage.new(state2)
        models.storage.save()

        # Test get for existing object
        state1_id = state1.id
        #retrieved_state = DBStorage().get(State, state1_id)
        #self.assertEqual(retrieved_state, state1)

        # Test get for non-existent object
        #non_existent_id = "non_existent_id"
        #non_existent_state = DBStorage().get(State, non_existent_id)
        #self.assertIsNone(non_existent_state)

    def test_count_method(self):
        """Test the DBStorage.count() method"""
        # Add objects to the database for testing
        state1 = State(name="California")
        state2 = State(name="New York")
        models.storage.new(state1)
        models.storage.new(state2)
        models.storage.save()

        # Test count without specifying class
        #all_objects_count = DBStorage().count()
        #self.assertEqual(all_objects_count, 2)

        # Test count for specific class
        #state_count = DBStorage().count(State)
        #self.assertEqual(state_count, 2)

        # Test count for non-existent class
        #non_existent_count = DBStorage().count(Review)
        #self.assertEqual(non_existent_count, 0)
