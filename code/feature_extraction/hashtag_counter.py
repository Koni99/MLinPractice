#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Count number of hashtags per tweet
Created on Fri Oct  8 11:45:03 2021

@author: kstroemel
"""
from code.feature_extraction.feature_extractor import FeatureExtractor
from code.util import COLUMN_HASHTAGS

class HashtagCounter(FeatureExtractor):
    #constructor
    def __init__(self, input_column):
        super().__init__([COLUMN_HASHTAGS],"{0}_number_of_hashtags".format(input_column))

    def _get_values(self, inputs):
        """Count number of hashtags."""
        hashtags = inputs.len()
        
        return hashtags
