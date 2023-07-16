#!/usr/bin/env python3

from sklearn.datasets import load_iris
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn import datasets
from sklearn.model_selection import train_test_split

def plant_classification():
    # load the iris data sets
    dataset = datasets.load_iris()
    X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target, train_size=0.8, random_state=0)
    gnb = GaussianNB()
    y_pred = gnb.fit(X_train, y_train).predict(X_test)
    score = accuracy_score(y_test, y_pred)
    return score

def main():
    print(f"Accuracy is {plant_classification()}")

if __name__ == "__main__":
    main()
