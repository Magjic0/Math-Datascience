import numpy as np
from sklearn.neighbors import KNeighborsClassifier

X = np.array([[0,0], [0,1], [1,0], [1,1]], dtype=float)
y = np.array([0, 0, 1, 1])

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)
print(knn.predict([[0.8, 0.9]]))