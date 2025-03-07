import numpy as np

def mean_shift(X, rayon=1.0, max_iter=100):
    X_shifted = np.copy(X)
    n, d = X_shifted.shape
    
    for _ in range(max_iter):
        new_positions = []
        for i in range(n):
            distances = np.linalg.norm(X_shifted - X_shifted[i], axis=1)
            voisins = X_shifted[distances < rayon]
            nouvelle_position = np.mean(voisins, axis=0)
            new_positions.append(nouvelle_position)
        
        new_positions = np.vstack(new_positions)
        deplacements = np.linalg.norm(X_shifted - new_positions, axis=1)
        X_shifted = new_positions
        if np.max(deplacements) < 1e-5:
            break
    
    return X_shifted

np.random.seed(0)
donnees_cluster1 = np.random.normal(loc=[0, 0], scale=0.5, size=(50, 2))
donnees_cluster2 = np.random.normal(loc=[5, 5], scale=0.5, size=(50, 2))
X_donnees = np.vstack([donnees_cluster1, donnees_cluster2])

positions_finales = mean_shift(X_donnees, rayon=1.2, max_iter=100)
print("Positions finales")
print(positions_finales[:5])
