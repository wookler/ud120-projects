#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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
###features_train = features_train[:len(features_train)/100]
###labels_train = labels_train[:len(labels_train)/100]

#########################################################
### your code goes here ###

import numpy as np
from sklearn import svm
from sklearn.metrics import accuracy_score

def perdictAuthor():



	clf = svm.SVC(C = 10000, kernel = "rbf")

	t_start_train = time()

	clf.fit(features_train, labels_train)

	print "training time:", round(time()-t_start_train, 3), "s"

	t_start_pred = time()
	
	predictions = clf.predict(features_test)

	print "prediction time:", round(time()-t_start_pred, 3), "s"

	score = accuracy_score(labels_test, predictions)

	print score
	print predictions[10]
	print predictions[26]
	print predictions[50]

	chrisEmails = list(filter(lambda x : x == 1, predictions))
	print len(chrisEmails)

perdictAuthor()

#########################################################


