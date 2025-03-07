import numpy as np
from sklearn.cluster import KMeans

X = np.array([[1,2], [2,1], [8,9], [9,8]], dtype=float)
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)
print(kmeans.labels_)
print(kmeans.cluster_centers_)