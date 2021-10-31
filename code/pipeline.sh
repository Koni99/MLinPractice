#!/bin/bash
# overall pipeline for the ML experiments

echo "loading data"
code/load_data.sh
echo "preprocessing"
code/preprocessing.sh
echo "feature extraction"
code/feature_extraction.sh
echo "classification"
code/classification.sh