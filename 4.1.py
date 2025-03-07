import numpy as np
from sklearn.linear_model import LogisticRegression

X = np.array([[0], [1], [2], [3], [4]], dtype=float)
y = np.array([0, 0, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)
print(model.predict([[1.5]]))
