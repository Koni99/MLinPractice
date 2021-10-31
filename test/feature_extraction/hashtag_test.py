#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
unittest for HashtagCounter
Created on Sat Oct 30 14:17:54 2021

@author: mareil
"""

import unittest
import pandas as pd
from code.feature_extraction.hashtag_counter import HashtagCounter

class HashtagTest(unittest.TestCase):
    
    def setUp(self):
        self.INPUT_COLUMN = "input"
        self.hashtags = HashtagCounter(self.INPUT_COLUMN)
        self.df = pd.DataFrame()
        self.df[self.INPUT_COLUMN] = [['firstHashtag', 'secondHashtag']]
    
    # check whether the input columns match
    def test_input_columns(self):
        self.assertEqual(self.hashtags._input_columns, [self.INPUT_COLUMN])

    # check whether the feature names match  
    def test_feature_name(self):  
        self.assertEqual(self.hashtags.get_feature_name(), self.INPUT_COLUMN + "_number_of_hashtags")

    # check whether HashtagCounter returns the correct value of hashtags
    def test_if_number_of_hashtags_correct(self):
        hashtagcounter = self.hashtags.fit_transform(self.df)    
        expected_output = 2
        self.assertEqual(hashtagcounter[0][0], expected_output)
        

if __name__ == '__main__':
    unittest.main()