import numpy as np

def regression_polynomiale(X, y, degre):

    X = X.reshape(-1, 1)
    X_poly = [X**i for i in range(degre + 1)]
    X_poly = np.hstack(X_poly)

    XTX = X_poly.T @ X_poly
    XTy = X_poly.T @ y
    theta = np.linalg.inv(XTX).dot(XTy)

    return theta

X_donnees = np.array([1, 2, 3, 4, 5], dtype=float)
y_donnees = np.array([2.1, 3.9, 6.1, 8.1, 10.5], dtype=float)

parametres = regression_polynomiale(X_donnees, y_donnees, degre=2)
print(parametres)

