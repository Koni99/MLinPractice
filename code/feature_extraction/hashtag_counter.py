#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Count number of hashtags per tweet
Created on Fri Oct  8 11:45:03 2021

@author: kstroemel
"""
from code.feature_extraction.feature_extractor import FeatureExtractor
import numpy as np

class HashtagCounter(FeatureExtractor):
    #constructor
    def __init__(self, input_column):
        super().__init__([input_column],"{0}_number_of_hashtags".format(input_column))

    # don't need to fit, so don't overwrite _set_variables()
    
    # count number of hashtags
    def _get_values(self, inputs):
        hashtag_list = []

        for i in inputs[0]:
            result = len(i)
            hashtag_list.append(result)  

        hashtag_list = np.array(hashtag_list)
        hashtag_list = hashtag_list.reshape(-1,1)
        return hashtag_list