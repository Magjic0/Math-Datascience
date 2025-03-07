import numpy as np

def moindres_carres(X, y):

    XTX = np.dot(X.T, X)
    XTy = np.dot(X.T, y)
    theta = np.linalg.inv(XTX).dot(XTy)
    return theta

x_donnees = np.array([1, 2, 3, 4, 5], dtype=float)
y_donnees = np.array([3, 5, 7, 9, 11], dtype=float)

X_construit = np.column_stack((np.ones_like(x_donnees), x_donnees))

params = moindres_carres(X_construit, y_donnees)

print(params)
