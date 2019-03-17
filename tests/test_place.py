# -*- coding: utf-8 -*-

import unittest
import sys
import os.path as path 
sys.path.insert(0, path.abspath(path.join(__file__ ,"../..")))
from geograpy3.place import Place

class TestPlace(unittest.TestCase):
    def test_basic(self):
        p = Place(city='city', region='region',  country='country')
        self.assertEqual('city', p.city)
        self.assertEqual('region', p.region)
        self.assertEqual('country', p.country)
        