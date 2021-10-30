#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
unittest for lowercaser
Created on Sat Oct 30 16:20:51 2021

@author: mareil
"""
import unittest
import pandas as pd
from code.preprocessing.lower_case import LowerCase

class LowercaserTest(unittest.TestCase):
    
    def setUp(self):
        self.INPUT_COLUMN = "input"
        self.OUTPUT_COLUMN = "output"
        self.lowercaser = LowerCase(self.INPUT_COLUMN, self.OUTPUT_COLUMN)
    
    def test_input_columns(self):
        self.assertListEqual(self.lowercaser._input_columns, [self.INPUT_COLUMN])

    def test_output_column(self):
        self.assertEqual(self.lowercaser._output_column, self.OUTPUT_COLUMN)

    def test_lowercase_single_sentence(self):
        input_text = "This is an Example Sentence"
        output_text = "['this is an example sentence']"
        
        input_df = pd.DataFrame()
        input_df[self.INPUT_COLUMN] = [input_text]
        
        lowercased = self.lowercaser.fit_transform(input_df)
        self.assertEqual(lowercased[self.OUTPUT_COLUMN][0], output_text)
    

if __name__ == '__main__':
    unittest.main()