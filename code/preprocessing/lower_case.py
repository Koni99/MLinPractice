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
    """Turn the tokenized input into lower case and store in lowercased and tokenized column"""
    #constructor
    def __init__(self):
        """Initialize with the given input (tokenized text) and output column (lowercased and tokenized)."""
        super().__init__([COLUMN_TOKENIZED], COLUMN_LOWERCASED_AND_TOKENIZED)
    
    # don't need to implement _set_variables(), since no variables to set
    
    def _get_values(self, inputs):
        """Turn the tokenized tweet into lower case."""
        result = []
        for token in inputs[0]:
            lowercased_token = token.lower()
            result.append(lowercased_token)

        return result
    