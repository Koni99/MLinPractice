#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
unittest for VideoAdded
Created on Sat Oct 30 14:17:54 2021

@author: mareil
"""

import unittest
import pandas as pd
from code.feature_extraction.video_added import VideoAdded

class VideosTest(unittest.TestCase):
    
    def setUp(self):      
        self.INPUT_COLUMN = "input"
        self.videos = VideoAdded(self.INPUT_COLUMN)
        
        self.df = pd.DataFrame()
        self.df[self.INPUT_COLUMN] = [0]
    
    def test_input_columns(self):
    # test if input columns match    
        self.assertEqual(self.videos._input_columns, [self.INPUT_COLUMN])

    def test_feature_name(self):
    # test if feature name matches    
        self.assertEqual(self.videos.get_feature_name(), self.INPUT_COLUMN + "_video_added")

    def test_if_video_added_correct(self):
    # test if VideoAdded returns the correct value (if there is a video added or not)    
        videoadded = self.videos.fit_transform(self.df)
        expected_output = False
        self.assertEqual(videoadded[0][0], expected_output)
        

if __name__ == '__main__':
    unittest.main()