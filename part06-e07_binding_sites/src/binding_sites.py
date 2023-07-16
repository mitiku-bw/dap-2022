#!/usr/bin/env python3
 
import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances
 
from matplotlib import pyplot as plt
 
import seaborn as sns
sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc

# Converts a nucleotide to an integer. 
# Use the following mapping: A -> 0C -> 1G -> 2T -> 3
def toint(x):
    d=dict(zip("ACGT", range(4)))
    return d[x]
def get_features_and_labels(filename):
    # Get a filename as a parameter
    df = pd.read_csv(filename, sep='\t')
    y = df.y
    A = np.array(df.X.map(list).values.tolist())
    # Convert the column into a feature matrix using the toint function
    toint2 = np.vectorize(toint)
    A = toint2(A)
    return A, y
 
def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()
 
def cluster_euclidean(filename):
    # Get a filename as parameter
    A, y = get_features_and_labels(filename)

    # Perform hierarchical clustering using the function sklearn.cluster.AgglomerativeClustering
    model = AgglomerativeClustering(2, linkage="average", affinity='euclidean')
    yfitted = model.fit_predict(A)
    acc = accuracy_score(y, yfitted)
    return acc

# Create function cluster_hamming that works like the function in part 2, except now using the hamming affinity
def cluster_hamming(filename):
    A, y = get_features_and_labels(filename)
    distances = pairwise_distances(A, metric="hamming")

    # Even though it is possible to pass the function hamming to AgglomerativeClustering, let us now compute the Hamming distance matrix explicitly
    model = AgglomerativeClustering(2, linkage="average", affinity='precomputed')
    yfitted = 1 - model.fit_predict(distances)
    # plot(distances, "average", "hamming")
    return accuracy_score(y, yfitted)
 
 
def main():
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))
 
if __name__ == "__main__":
    main()