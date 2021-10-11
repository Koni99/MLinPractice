# Documentation

## Preprocessing

## Feature Extraction

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

We chose these evaluation metrics due to their respective properties, because they are good to use in our highly imbalanced data set (5% viral 95% not)

### Evaluation baseline
**Majority vote classifier**
- always predicts the majority class (in our case "not viral")

**Uniform distribution classifier**
- generates predictions uniformly at random

**Frequency classifier**
- generates random predictions respecting the training set class distribution (i.e. the label frequency)

## Application
