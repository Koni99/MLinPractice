#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Runs the specified collection of feature extractors.

Created on Wed Sep 29 11:00:24 2021

@author: lbechberger
"""

import argparse, csv, pickle
import pandas as pd
import numpy as np
from code.feature_extraction.character_length import CharacterLength
from code.feature_extraction.stopwords_counter import StopwordsCounter
from code.feature_extraction.photo_added import PhotoAdded
from code.feature_extraction.video_added import VideoAdded
from code.feature_extraction.feature_collector import FeatureCollector
from code.feature_extraction.sentiment_analysis import SentimentAnalysis
from code.feature_extraction.hashtag_counter import HashtagCounter 
from code.util import COLUMN_TWEET, COLUMN_LABEL, COLUMN_HASHTAGS, COLUMN_PHOTOS, COLUMN_VIDEO, COLUMN_LOWERCASED_AND_TOKENIZED

# setting up CLI
parser = argparse.ArgumentParser(description = "Feature Extraction")
parser.add_argument("input_file", help = "path to the input csv file")
parser.add_argument("output_file", help = "path to the output pickle file")
parser.add_argument("-e", "--export_file", help = "create a pipeline and export to the given location", default = None)
parser.add_argument("-i", "--import_file", help = "import an existing pipeline from the given location", default = None)
parser.add_argument("-c", "--char_length", action = "store_true", help = "compute the number of characters in the tweet")
parser.add_argument("-st", "--stopwords", action = "store_true", help = "count number of stopwords")
parser.add_argument("-s", "--sentiment", action = "store_true", help = "compute the compound sentiment score in the tweet")
parser.add_argument("-ha", "--hashtags", action = "store_true", help = "count the number of hashtags in the tweet")
parser.add_argument("-p", "--photo_added", action = "store_true", help = "check whether tweet has a photo added")
parser.add_argument("-v", "--video_added", action = "store_true", help = "check whether tweet has a video added")
args = parser.parse_args()

# load data
df = pd.read_csv(args.input_file, quoting = csv.QUOTE_NONNUMERIC, lineterminator = "\n")

if args.import_file is not None:
    # simply import an exisiting FeatureCollector
    with open(args.import_file, "rb") as f_in:
        feature_collector = pickle.load(f_in)

else:    # need to create FeatureCollector manually

    # collect all feature extractors
    features = []
    if args.char_length:
        # character length of original tweet (without any changes)
        features.append(CharacterLength(COLUMN_TWEET))
    if args.stopwords:
        # count number of stopwords
        features.append(StopwordsCounter(COLUMN_LOWERCASED_AND_TOKENIZED))
    if args.photo_added:
        # check whether tweet has a photo added
        features.append(PhotoAdded(COLUMN_PHOTOS))
    if args.video_added:
        # check whether tweet has a video added
        features.append(VideoAdded(COLUMN_VIDEO))
    if args.sentiment:
        # compound sentiment score of original tweet (without any changes)
        features.append(SentimentAnalysis(COLUMN_TWEET))
    if args.hashtags:
        # count number of hastags of tweet
        features.append(HashtagCounter(COLUMN_HASHTAGS))
    # create overall FeatureCollector
    feature_collector = FeatureCollector(features)
    
    # fit it on the given data set (assumed to be training data)
    feature_collector.fit(df)


# apply the given FeatureCollector on the current data set
# maps the pandas DataFrame to an numpy array
feature_array = feature_collector.transform(df)

# get label array
label_array = np.array(df[COLUMN_LABEL])
label_array = label_array.reshape(-1, 1)

# store the results
results = {"features": feature_array, "labels": label_array, 
           "feature_names": feature_collector.get_feature_names()}
with open(args.output_file, 'wb') as f_out:
    pickle.dump(results, f_out)

# export the FeatureCollector as pickle file if desired by user
if args.export_file is not None:
    with open(args.export_file, 'wb') as f_out:
        pickle.dump(feature_collector, f_out)
