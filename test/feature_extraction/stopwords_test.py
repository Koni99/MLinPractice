#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
unittest for stopwords counter
Created on Sun Oct 31 08:13:42 2021

@author: mareil
"""

import unittest
import pandas as pd
from code.feature_extraction.stopwords_counter import StopwordsCounter

class StopwordsTest(unittest.TestCase):
    
    def setUp(self):
        self.INPUT_COLUMN = "input"
        self.stopwords = StopwordsCounter(self.INPUT_COLUMN)
        
        self.df = pd.DataFrame()
        self.df[self.INPUT_COLUMN] = [['this', 'is', 'a', 'tokenized', 'and', 'lowercased', 'tweet']]
    
    def test_input_columns(self):
    # check whether the input columns match    
        self.assertEqual(self.stopwords._input_columns, [self.INPUT_COLUMN])

    def test_feature_name(self):
    # check whether the feature names match    
        self.assertEqual(self.stopwords.get_feature_name(), self.INPUT_COLUMN + "_number_of_stopwords")

    def test_if_number_of_stopwords_correct(self):
    # check whether StopwordsCounter returns the correct value of hashtags
        stopwordscounter = self.stopwords.fit_transform(self.df)    
        expected_output = 4
        self.assertEqual(stopwordscounter[0][0], expected_output)
        

if __name__ == '__main__':
    unittest.main()