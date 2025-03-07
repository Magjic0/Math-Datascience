import numpy as np

def regression_brute(X_donnees, y_donnees, resolution=10):
    a_opt, b_opt = None, None
    erreur_min = float('inf')
    
    valeurs_a = np.linspace(-5, 5, resolution)
    valeurs_b = np.linspace(-5, 5, resolution)
    
    for a in valeurs_a:
        for b in valeurs_b:
            y_pred = a * X_donnees + b
            erreur = np.mean((y_donnees - y_pred)**2)
            if erreur < erreur_min:
                erreur_min = erreur
                a_opt, b_opt = a, b
    
    return a_opt, b_opt, erreur_min

X_donnees = np.array([1, 2, 3, 4, 5], dtype=float)
y_donnees = np.array([2, 4, 5, 6, 8], dtype=float)

a, b, erreur = regression_brute(X_donnees, y_donnees, resolution=50)
print("a =", a, "b =", b, "erreur =", erreur)