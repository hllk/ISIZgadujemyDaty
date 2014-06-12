# -*- coding: utf-8 -*-

import codecs
from text.classifiers import NaiveBayesClassifier

#training - years
inputfile = codecs.open("years-train.txt", 'r', 'utf-8')
years_train = inputfile.readlines()
inputfile.close()

#training - content
inputfile = codecs.open("contents-train.txt", 'r', 'utf-8')
contents_train = inputfile.readlines()
inputfile.close()

#dev - years
inputfile = codecs.open("years-dev.txt", 'r', 'utf-8')
dev_train = inputfile.readlines()
inputfile.close()

#dev - content
inputfile = codecs.open("contents-dev.txt", 'r', 'utf-8')
contents_dev = inputfile.readlines()
inputfile.close()

#training set
train_set = []
g = range(0, 4000, 2)
for i in g:
	train_set.append((contents_train[i], years_train[i/2]))


print "tu się robi"	
cl = NaiveBayesClassifier(train_set)
print "a tu się zrobiło"
outputfile = open("classified.txt", "w")
g = range(0, len(contents_dev), 2)
for i in g:
	result = cl.classify(contents_dev[i])
	print i
	outputfile.write(str(result))
print "zmieliło"
outputfile.close()

