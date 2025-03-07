import numpy as np

def descente_de_gradient(fonction, grad_fonction, point_depart, pas=0.1, nb_iterations=100):

    x = point_depart
    for _ in range(nb_iterations):
        gradient = grad_fonction(x)
        x = x - pas * gradient
    return x

def fonction(a):
    return (a - 3)**2 + 2

def grad_fonction(a):
    return 2*(a - 3)

minimum = descente_de_gradient(fonction,grad_fonction,point_depart=10.0,pas=0.1,nb_iterations=50)
print(minimum)
