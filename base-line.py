#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
import string
from collections import Counter
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import collections
import re, csv, codecs


def get_tokens(text):
    text = unicode(text).encode('ascii', 'replace')
    lowers = text.lower()
    no_punctuation = lowers.translate(None, string.punctuation)
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens

trainPath = "../retroc-train-cleaned-500w.xml"
devPath = "../retroc-dev-cleaned-500w.xml"
inputfileTrain = codecs.open(trainPath, 'r', 'utf-8')
inputfileDev = codecs.open(devPath, 'r', 'utf-8')
giantfileTrain = inputfileTrain.readlines()
giantfileDev = inputfileDev.readlines()
inputfileTrain.close()
inputfileDev.close()

portions = collections.OrderedDict()

for i in range(len(giantfileTrain)):
    line = giantfileTrain[i]
    if "<date annee=" in line:
        xxx = re.search(r'\d\d\d\d', line).group(0)
        if not (portions.has_key(xxx)):
            portions[xxx] = "";
        for j in range(i, i + 5, 1):
            if "<texte>" in giantfileTrain[j]:
                portions[xxx] += giantfileTrain[j+1] 
                i = i+5
                break

tfidf = TfidfVectorizer(tokenizer=get_tokens, stop_words=stopwords.words('polish'))
tfs = tfidf.fit_transform(portions.values())


yearsDev = [];
contentsDev = [];
for i in range(len(giantfileDev)):
    line = giantfileDev[i]
    if "<date annee=" in line:
        xxx = re.search(r'\d\d\d\d', line).group(0)
        yearsDev.append(xxx)
        for j in range(i, i + 5, 1):
            if "<texte>" in giantfileDev[j]:
                contentsDev.append(giantfileDev[j+1])
                i = i+5
                break



for i in range(len(contentsDev)):
    response = tfidf.transform([contentsDev[i]])
    result = cosine_similarity(response, tfs)
    index = result.tolist()[0].index(max(result.tolist()[0]))
    print yearsDev[i] + ',' + (portions.items()[index])[0]
