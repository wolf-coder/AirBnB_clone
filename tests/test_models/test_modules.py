#!/usr/bin/python3
"""
Testing the user (user.py) model.
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class Test_modules(unittest.TestCase):
    """
    Testing modules: amenity, city, places, review, stat
    """
    def test_amenity(self):
        """
        Testing Amenity: 'name' class attribute
        """
        self.assertIn("name", Amenity.__dict__)
        self.assertTrue(type(Amenity.name) == str)

    def test_city(self):
        """
        Testing Amenity: state_id, name class attribute exists
        """
        self.assertIn('state_id', City.__dict__)
        self.assertIn('name', City.__dict__)

    def test_place(self):
        """
        Testing all requiered class attribute exists.
        """
        self.assertIn("name", Place.__dict__)
        self.assertIn("city_id", Place.__dict__)
        self.assertIn("user_id", Place.__dict__)
        self.assertIn("name", Place.__dict__)
        self.assertIn("description", Place.__dict__)
        self.assertIn("number_rooms", Place.__dict__)
        self.assertIn("number_bathrooms", Place.__dict__)
        self.assertIn("max_guest", Place.__dict__)
        self.assertIn("price_by_night", Place.__dict__)
        self.assertIn("latitude", Place.__dict__)
        self.assertIn("longitude", Place.__dict__)
        self.assertIn("amenity_ids", Place.__dict__)

    def test_Review(self):
        """
        Testing Review class attributes existence.
        """
        self.assertIn("text", Review.__dict__)
        self.assertIn("place_id", Review.__dict__)
        self.assertIn("user_id", Review.__dict__)

    def test_State(self):
        """
        Testing State class attributes existence.
        """
        self.assertIn("name", State.__dict__)


if __name__ == '__main__':
    unittest.main()
