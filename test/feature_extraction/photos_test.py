#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
unittest for PhotoAdded
Created on Sat Oct 30 14:17:54 2021

@author: mareil
"""

import unittest
import pandas as pd
from code.feature_extraction.photo_added import PhotoAdded

class PhotosTest(unittest.TestCase):
    
    def setUp(self):
        self.INPUT_COLUMN = "input"
        self.photos = PhotoAdded(self.INPUT_COLUMN)
        
        self.df = pd.DataFrame()
        self.df[self.INPUT_COLUMN] = [['https://example.com']]
    
    def test_input_columns(self):
    # check whether the input columns match    
        self.assertEqual(self.photos._input_columns, [self.INPUT_COLUMN])

    def test_feature_name(self):
    # check whether the feature names match    
        self.assertEqual(self.photos.get_feature_name(), self.INPUT_COLUMN + "_photo_added")

    def test_if_photo_added_correct(self):
    # check whether PhotoAdded returns the correct value (if photo is added or not)    
        photoadded = self.photos.fit_transform(self.df)
        expected_output = True
        self.assertEqual(photoadded[0][0], expected_output)
        

if __name__ == '__main__':
    unittest.main()