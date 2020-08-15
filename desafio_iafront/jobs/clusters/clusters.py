import numpy as np
from sklearn.cluster import KMeans, estimate_bandwidth
from sklearn.cluster import \
    mean_shift as _mean_shift, \
    spectral_clustering as _spectral_clustering, \
    cluster_optics_dbscan as _optics, \
    dbscan as _dbscan


def kmeans(vector: np.array, n: int):
    k = KMeans(n_clusters=n, random_state=0)
    cluster_coordinate = k.fit_transform(vector)
    cluster_label = k.fit(vector)

    return cluster_coordinate, cluster_label.labels_


def spectral_clustering(vector: np.array, n: int):
    return _spectral_clustering(vector, n_clusters=n, affinity='precomputed', random_state=0, assign_labels='discretize')


def mean_shift(vector: np.array):
    bandwidth = estimate_bandwidth(vector)
    return _mean_shift(bandwidth=bandwidth, bin_seeding=True)


def optics(vector: np.array):
    return _optics(vector)


def dbscan(vector: np.array):
    return _dbscan(vector)
