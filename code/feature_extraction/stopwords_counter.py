#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
count number of stopwords
Created on Sun Oct 31 07:32:55 2021

@author: mareil
"""
from code.feature_extraction.feature_extractor import FeatureExtractor
import numpy as np
from nltk.corpus import stopwords

class StopwordsCounter(FeatureExtractor):
    #constructor
    def __init__(self, input_column):
        super().__init__([input_column],"{0}_number_of_stopwords".format(input_column))

    def _get_values(self, inputs):
        """Count number of stopwords"""
        stop_words = set(stopwords.words('english'))
        
        stopwords_counts = []

        for i in inputs[0]:
        # filter all stopwords of one tweet, count the number of stopwords    
            stp_one_tweet = []
            
            for word in i:
                if(word in stop_words):
                    stp_one_tweet.append(word)
  
            stopwords_counts.append(len(stp_one_tweet))

        stopwords_counts = np.array(stopwords_counts)
        stopwords_counts = stopwords_counts.reshape(-1,1)
        return stopwords_counts