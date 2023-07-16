#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection
from sklearn.feature_extraction.text import CountVectorizer 


alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines

def get_features(a):
    vectorizer = CountVectorizer(analyzer='char_wb',
      vocabulary=alphabet)   
    X = vectorizer.fit_transform(a)
    result = X.toarray()
    return result

def contains_valid_chars(s):
    if set(s).issubset(alphabet_set):
        return True
    return False

def get_features_and_labels():
    #helper functions for filtering 
    def fin_helper(s):
        return contains_valid_chars(s.lower())
 
    def eng_helper(s):
        if s[0].isupper():
            return False
        return fin_helper(s)
 
    #filter words and combine 
    finnish = list(filter(fin_helper, load_finnish()))
    english = list(filter(eng_helper, load_english()))
    X = np.vstack((get_features(finnish), get_features(english)))
 
    #get target labels 
    y_fin = np.zeros((len(finnish),1), dtype=int)
    y_eng = np.ones((len(english),1), dtype=int)
    y = np.vstack((y_fin,y_eng))
    return X, y


def word_classification():
    model = MultinomialNB()
    X, y = get_features_and_labels()
    # Change the shape of y to n_samples
    cval = cross_val_score(model, X, np.ravel(y), cv=model_selection.KFold(n_splits=5, shuffle=True, random_state=0))
    print(cval)
    return cval

def main():
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()
