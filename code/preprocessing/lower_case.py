#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Function to turn the text into lower case
Created on Thu Oct  7 15:42:06 2021

@author: kstroemel
"""

from code.preprocessing.preprocessor import Preprocessor

class LowerCase(Preprocessor):
    """Turn the text input into lower case."""
    #constructor
    def __init__(self, input_column, output_column):
        """Initialize with the given input (tweet) and output column (tweet_lower_case)."""
        super().__init__([input_column], output_column)
    
    # don't need to implement _set_variables(), since no variables to set
    
    def _get_values(self, inputs):
        """Turn the tweet into lower case."""
        result = []
        for tweet in inputs[0]:
            lowercased_tweet = [tweet.lower()]
            result.append(str(lowercased_tweet))
        
        return result
    