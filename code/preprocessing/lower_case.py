#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Function to turn the tokenized input into lower case
Created on Thu Oct  7 15:42:06 2021

@author: kstroemel
"""

from code.preprocessing.preprocessor import Preprocessor
from code.util import COLUMN_TOKENIZED, COLUMN_LOWERCASED_AND_TOKENIZED

class LowerCase(Preprocessor):
    #constructor
    def __init__(self):
        # input is column with tokenized tweet, output gets stored in column_lowercased_and_tokenized
        super().__init__([COLUMN_TOKENIZED], COLUMN_LOWERCASED_AND_TOKENIZED)
    
    # don't need to implement _set_variables(), since no variables to set
    
    # turn the tokenized tweet into lower case
    def _get_values(self, inputs):
        result = []
        for token in inputs[0]:
            lowercased_token = token.lower()
            result.append(lowercased_token)

        return result
    