 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sentiment analysis: Every tweet gets a sentiment score ranging between -1 and 1.
-1 meaning very negative, 0 neutral and 1 very positive 
Created on Thu Oct  7 17:24:23 2021

@author: kstroemel
"""
import nltk
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download("vader_lexicon")
from code.feature_extraction.feature_extractor import FeatureExtractor

#class for our sentiment analyser
class SentimentAnalysis(FeatureExtractor):
    #constructor
    # double check that not sure about output name
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_sentiment_score".format(input_column))
    
    # don't need to fit, so don't overwrite _set_variables()
    
    # compute the sentiment score based on the inputs
    def _get_values(self, inputs):       
        sentiment = SentimentIntensityAnalyzer()
        result = []
        for tweet in inputs[0]:
            score = sentiment.polarity_scores(tweet)
            # we are only interested in the compound score
            result.append(score["compound"])
        result = np.array(result)
        result = result.reshape(-1,1)
        return result
        
        

        
    

