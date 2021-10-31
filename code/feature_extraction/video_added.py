#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check whether there is at least one video added
Created on Fri Oct 29 11:23:49 2021

@author: mareil
"""

from code.feature_extraction.feature_extractor import FeatureExtractor
import numpy as np

class VideoAdded(FeatureExtractor):
    
    #constructor
    def __init__(self, input_column):   
        super().__init__([input_column], "{0}_video_added".format(input_column))
        
    # don't need to fit, so don't overwrite _set_variables()
    
    #check whether there is at least one video
    def _get_values(self, inputs):
        video_list = []

        for i in inputs[0]:
            if (i == 0):
                result = False
            else:
                result = True
            
            video_list.append(result)
        
        video_list = np.array(video_list)
        video_list = video_list.reshape(-1,1)
        
        return video_list
                

