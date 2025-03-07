import numpy as np
from sklearn.ensemble import RandomForestRegressor

X = np.array([[1], [2], [3], [4], [5]], dtype=float)
y = np.array([2, 4, 5, 6, 8], dtype=float)

forest = RandomForestRegressor(n_estimators=10, max_depth=2)
forest.fit(X, y)
print(forest.predict([[3.5]]))
