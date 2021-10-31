#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
unittest for sentiment analysis
Created on Sat Oct 30 14:17:54 2021

@author: mareil
"""

import unittest
import pandas as pd
from code.feature_extraction.sentiment_analysis import SentimentAnalysis

class SentimentTest(unittest.TestCase):
    
    def setUp(self):
        self.INPUT_COLUMN = "input"
        self.sentiment = SentimentAnalysis(self.INPUT_COLUMN)
        self.df = pd.DataFrame()
        self.df[self.INPUT_COLUMN] = ["This is a good tweet"]
    
    # check whether the input columns match 
    def test_input_columns(self):   
        self.assertEqual(self.sentiment._input_columns, [self.INPUT_COLUMN])

    # check whether the feature names match     
    def test_feature_name(self):   
        self.assertEqual(self.sentiment.get_feature_name(), self.INPUT_COLUMN + "_sentiment_score")

    # check whether SentimentAnalysis returns correct sentiment score (calculated in seperate jupyter notebook)
    def test_if_right_sentiment_score(self):
        sentimentAnalysed = self.sentiment.fit_transform(self.df)
        # the respective scores that we calculated manually
        expected_output = 0.4404
        self.assertEqual(sentimentAnalysed[0][0], expected_output)
        

if __name__ == '__main__':
    unittest.main()

