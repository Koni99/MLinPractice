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
    
    def test_input_columns(self):
    # check whether the input columns match    
        self.assertEqual(self.sentiment._input_columns, [self.INPUT_COLUMN])

    def test_feature_name(self):
    # check whether the feature names match    
        self.assertEqual(self.sentiment.get_feature_name(), self.INPUT_COLUMN + "_sentiment_score")

    def test_if_right_sentiment_score(self):
    # check whether SentimentAnalysis returns correct sentiment score (calculated in seperate jupyter notebook)
        sentimentAnalysed = self.sentiment.fit_transform(self.df)
        # the respective scores that we calculated manually
        expected_output = 0.4404
        self.assertEqual(sentimentAnalysed[0][0], expected_output)
        

if __name__ == '__main__':
    unittest.main()

