# Documentation

## Preprocessing
**Lower case**
- turns every word in the tweet into lower case. Otherwise our classifier would think of e.g. "Dog" and "dog" as two completly different words.

## Feature Extraction
**Sentiment Analysis**
- added compound sentiment score as a feature. We argue that the sentiment of a tweet has an influence on its virality. 
- we used nltk.VADER which is specifically attuned to sentiments expressed in social media
- our function returns a score between -1 very negative and 1 very positive.
- our hypothesis is that tweets that are in the outer range either very negative or very positive will be more popular than neutral tweets with scores around 0.

## Dimensionality Reduction

## Classification

### Evaluation metrics
**Accuracy**
- total number of correct predictions divided by total number of predictions in the data set
- default implementation but inappropriate due to imbalanced data set

**Balanced Accuracy**
- arithmetic mean of precision (number of positive class predictions that actually belong to the positive class) and recall (positive class predictions made out of all positive examples)
- variant of accuracy metric that is more appropriate for imbalanced data sets

**F1 Score**
- balances precision and recall in a single number
- f1 considers false positives and false negatives as equally important
- appropriate for imbalanced data sets
- generally better scoring metric than *balanced accuracy* for imbalanced data when more attention on the positives is needed (in our case: tweets predicted as viral)

**Cohen's Kappa**
- measures interrater reliability (reliability for two raters that are rating the same thing, corrected for how often that the raters may agree by chance)
- appropriate for imbalanced data sets

### Evaluation baseline

**Uniform distribution classifier**
- generates predictions uniformly at random

**Stratified classifier**
- generates random predictions by respecting the training set class distribution -> label frequency

## Application
