#!/usr/bin/env python3
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import gzip
 
def spam_detection(random_state=0, fraction=1.0):
    fraction_of_ham = []
    # Read the lines from the files into arrays
    with gzip.open('src/ham.txt.gz','r') as ham:
        ham_lines = ham.readlines()
        n = int(len(ham_lines)*fraction)
        fraction_of_spam = []
        for line in range(1, 1 + n ):
            if line < n or (line==n and random_state > 0):
                fraction_of_ham.append(ham_lines[line])
    with gzip.open('src/spam.txt.gz','r') as spam:
        spam_lines = spam.readlines()
        n2 = int(len(spam_lines)*fraction)
        for line in range(1, 1 + n2):
            if line < n2 or (line==n2 and random_state > 0):
                fraction_of_spam.append(spam_lines[line])

    # form the combined feature matrix
    # use labels 0 for ham and 1 for spam
    data_ham_spam = np.concatenate([fraction_of_ham, fraction_of_spam])
 
    t_ham = np.zeros(len(fraction_of_ham))
    t_spam = np.ones(len(fraction_of_spam))
    target = np.concatenate([t_ham, t_spam])
 
    vectorizer = CountVectorizer()
    data = vectorizer.fit_transform(data_ham_spam)
    data = data.toarray()
 
    X_train, X_test, y_train, y_test = train_test_split(data, target, train_size = 0.75, random_state = random_state)
    model = MultinomialNB()
    model.fit(X_train, y_train)
    label_predicted = model.predict(X_test)
 
    accuracy = metrics.accuracy_score(y_test, label_predicted)
    size_of_test_sample = len(y_test)
    misclassified = int(len(y_test)*(1 - accuracy))
    return accuracy, size_of_test_sample, misclassified
 
def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")
 
if __name__ == "__main__":
    main()