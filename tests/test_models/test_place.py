#!/usr/bin/python3
"""
Testing the user (user.py) model.
"""
import unittest
from models.place import Place, BaseModel


class Test_modules(unittest.TestCase):
    """
    Testing modules: state
    """
    def test_Place(self):
        """
        Testing State: 'name' class attribute
        """
        self.assertTrue(issubclass(Place, BaseModel))

        self.assertTrue(type(Place.name) == str)
        self.assertTrue(type(Place.city_id) == str)
        self.assertTrue(type(Place.user_id) == str)
        self.assertTrue(type(Place.name) == str)
        self.assertTrue(type(Place.description) == str)
        self.assertTrue(type(Place.number_rooms) == int)
        self.assertTrue(type(Place.number_bathrooms) == int)
        self.assertTrue(type(Place.max_guest) == int)
        self.assertTrue(type(Place.price_by_night) == int)
        self.assertTrue(type(Place.latitude) == float)
        self.assertTrue(type(Place.longitude) == float)
        self.assertTrue(type(Place.amenity_ids) == list)


if __name__ == '__main__':
    unittest.main()
