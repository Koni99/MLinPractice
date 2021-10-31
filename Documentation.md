# Documentation

## Preprocessing
**Lowercaser**
- turns every word in the tweet into lower case. Otherwise our classifier would think of e.g. "Dog" and "dog" as two completly different words.
- the lowercased and tokenized tweet later operates as input to the stopwords counter. Lowercased words can be detected as stopwords.

## Feature Extraction
**Sentiment Analysis**
- added compound sentiment score as a feature. We argue that the sentiment of a tweet has an influence on its virality. 
- we used nltk.VADER which is specifically attuned to sentiments expressed in social media.
- our function returns a score between -1 very negative and 1 very positive.
- our hypothesis is that tweets that are in the outer range either very negative or very positive will be more popular than neutral tweets with scores around 0.

**Hashtag Counter**
- count number of hashtags.
- we assume that tweets with many hashtags attract more attention than tweets without hashtags, as tweets with hashtags added can be found additionally via that hashtag.

**Detect Photos**
- checks whether a tweet has a photo added.
- we assume that tweets with photos added will be more popular than pure text.

**Detect Videos**
- checks whether there is a video added to a tweet.
- we assume that tweets with videos attract more attention than those without.

**Stopwords Counter**
- counts the stopwords that occur in a tweet.
- less stopwords like e.g. "the" or "a" means more information is packed into the tweet, as the total number of words is restricted. Tweets don't have to always be gramatically correct, but are sometimes rather structured in bullet points. We think this might have an impact on the popularity of the tweet.

## Dimensionality Reduction
- we don't need dimensionality reduction due to small number of features.

## Classification

### Evaluation metrics
**Accuracy**
- total number of correct predictions divided by total number of predictions in the data set.
- default implementation but inappropriate due to imbalanced data set.

**Balanced Accuracy**
- arithmetic mean of precision (number of positive class predictions that actually belong to the positive class) and recall (positive class predictions made out of all positive examples).
- variant of accuracy metric that is more appropriate for imbalanced data sets.

**F1 Score**
- balances precision and recall in a single number
- f1 considers false positives and false negatives as equally important
- appropriate for imbalanced data sets
- generally better scoring metric than *balanced accuracy* for imbalanced data when more attention on the positives is needed (in our case: tweets predicted as viral)

**Cohen's Kappa**
- measures interrater reliability (reliability for two raters that are rating the same thing, corrected for how often that the raters may agree by chance)
- appropriate for imbalanced data sets

We chose these evaluation metrics due to their respective properties, because they are good to use in our highly imbalanced data set (9% viral 91% not)

### Evaluation baseline
**Majority vote classifier**
- always predicts the majority class (in our case "not viral")

**Uniform distribution classifier**
- generates predictions uniformly at random

**Frequency classifier**
- generates random predictions respecting the training set class distribution (i.e. the label frequency)

**KNN classifier**
- predicts class due to k closest training examples in the data set

## Hyperparameter Optimization
**KNN classifier grid search**
k: number of neighbours    
Scores for accurcay and balanced accuracy in percent (between 0 and 100%).   
Scores for Cohen's Kappa and F1 Score between 0 and 1.   
Respective score on training set / validation set   

| k  | Accuracy |Cohen's Kappa |F1 |Balanced Accuracy|
|---|---|---|---|---|
| 1 |82.87 / 82.78|0.0227 / 0.0237|0.1173 / 0.1188|51.12 / 51.26|
| 2 |90.01 / 90.03|0.0119 / 0.0138|0.0319 / 0.0337|50.36 / 50.42|
| 3 |87.34 / 87.39|0.0356 / 0.0415|0.0967 / 0.1025|51.40 / 51.64|
| 4 |89.99 / 89.93|0.0144 / 0.0114|0.0353 / 0.0328|50.44 / 50.35|
| 5 |89.10 / 89.14|0.0240 / 0.0266|0.0615 / 0.0638|50.80 / 50.89|
| 6 |90.82 / 90.82|0.0000 / 0.0000|0.0000 / 0.0000|50.00 / 50.00|
| 7 |89.97 / 89.92|0.0138 / 0.0143|0.0350 / 0.0365|50.42 / 50.44|
| 8 |90.40 / 90.36|0.0104 / 0.0089|0.0220 / 0.0213|50.30 / 50.26|
| 9 |90.40 / 90.36|0.0104 / 0.0089|0.0220 / 0.0213|50.30 / 50.26|
|10 |90.40 / 90.36|0.0104 / 0.0089|0.0220 / 0.0213|50.30 / 50.26|   

After the grid search we decided to use KNN with 3 nearest neighbours, because it got the highest Cohen's Kappa score, highest balanced accuracy and second highest F1 score.   

## Results  
Now we want to evaluate our ML model in comparison to our three baseline classifiers.  

**Training set** 
|Classifier| Accuracy |Cohen's Kappa |F1 |Balanced Accuracy|
|---|---|---|---|---|
|Majority vote|90.82|0.0000|0.0000|50.00|
|Label frequency|83.46|0.0043|0.09547|50.22|
|Uniform distribution|50.05|0.0014|0.1563|50.21|
|K-nearest neighbours|87.34|0.0356|0.0967|51.40|   

**Validation set** 
|Classifier| Accuracy |Cohen's Kappa |F1 |Balanced Accuracy|
|---|---|---|---|---|
|Majority vote|90.82|0.0000|0.0000|50.00|
|Label frequency|83.27|-0.0048|0.0873|49.76|
|Uniform distribution|50.08|-8.2331|0.1550|49.98|
|K-nearest neighbours|87.39|0.0415|0.1025|51.64|   

**Test set** 
|Classifier| Accuracy |Cohen's Kappa |F1 |Balanced Accuracy|
|---|---|---|---|---|
|Majority vote|90.82|0.0000|0.0000|50.00|
|Label frequency|83.37|0.0007|0.0922|50.03|
|Uniform distribution|50.03|-0.0010|0.1542|49.99|
|K-nearest neighbours|87.22|0.0286|0.0904|51.13|   

**Discussion**   
Because our data set is highly imbalanced the majority vote classifier still achieves the highest accuracy. But our KNN model reaches the highest balanced accuracy and Cohen's Kappa score on training, validation and test set. All in all there is still a lot of room for improvements. That is due to the fact that we did not implement many features and also tried only a few preprocessing steps. In future works one could for example try to add features based on the POS (part-of-speech) tag and count the number of adjectives and adverbs in a tweet or use the metadata like time of the day it was published. 

