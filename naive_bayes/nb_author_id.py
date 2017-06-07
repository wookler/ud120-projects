#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
### create a new classifier
### create predictions based on input test features using the predict function
### estimate accuracy using accuracy_score function
#########################################################
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

def predictAuthor():
	### create a new classifier
	clf = GaussianNB()

	### start clock
	t_start_train = time()

	### train the classifier with training features and labels
	clf.fit(features_train, labels_train)

	###output learning time
	print "training time:", round(time()-t_start_train, 3), "s"

	t_start_predict = time()

	### create predictions based on input test features using the predict function
	predictions = clf.predict(features_test)

	print "prediction time:", round(time()-t_start_predict, 3), "s"

	### estimate accuracy using accuracy_score function
	accuracy = accuracy_score(labels_test, predictions)

	print accuracy


predictAuthor()