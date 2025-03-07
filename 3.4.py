import numpy as np
from sklearn.tree import DecisionTreeRegressor

X = np.array([[1], [2], [3], [4], [5]], dtype=float)
y = np.array([2, 4, 5, 6, 8], dtype=float)

tree = DecisionTreeRegressor(max_depth=2)
tree.fit(X, y)
print(tree.predict([[3.5]]))