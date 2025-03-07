import numpy as np

def regression_lineaire_analytique(X, y):

    XTX = np.dot(X.T, X)
    XTy = np.dot(X.T, y)
    theta = np.linalg.inv(XTX).dot(XTy)
    return theta

X_exemples = np.array([[1, 1],
                       [1, 2],
                       [1, 3],
                       [1, 4]], dtype=float)
y_exemples = np.array([2, 4, 6, 8], dtype=float)

parametres = regression_lineaire_analytique(X_exemples, y_exemples)
print(parametres)