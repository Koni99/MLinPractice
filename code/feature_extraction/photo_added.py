#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check whether input tweet has at least one photo added.
Created on Mon Oct 11 15:32:10 2021

@author: mareil
"""

from code.feature_extraction.feature_extractor import FeatureExtractor
from code.util import COLUMN_PHOTOS

class PhotoAdded(FeatureExtractor):
    # constructor
    def __init__(self, input_column):
        super().__init__([COLUMN_PHOTOS], "{0}_photo_added".format(input_column))
        
        
    def get_values(self, inputs):
    # check whether there is at least one photo
        photo_list = []
        
        for i in inputs[0]:
            if (i.len() == 0):
                result = False
            else:
                result = True
            photo_list.append(result)  
        
        photo_list = np.array(photo_list)
        photo_list = photo_list.reshape(-1,1)
        return photo_list