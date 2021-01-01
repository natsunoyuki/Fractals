import numpy as np
import matplotlib.pyplot as plt
from scipy import random

def sierpins(N):
    """
    This function generates the sierpinski triangle fractal
    
    Input
    -----
    N: int
        number of points to generate
        
    Returns
    -------
    X: np.array
        np.array of points of the cantor box
    """    
    X = np.zeros([N + 1, 2])

    for k in range(N):
        r = random.random()
        if r <= 1.0 / 3.0:
            X[k + 1, 0] = 0.5 * X[k, 0]
            X[k + 1, 1] = 0.5 * X[k, 1]
        elif r <= 2.0 / 3.0:
            X[k + 1, 0] = 0.5 * X[k, 0] + 0.25
            X[k + 1, 1] = 0.5 * X[k, 1] + np.sqrt(3) / 4.0
        else:
            X[k + 1, 0] = 0.5 * X[k, 0] + 0.5
            X[k + 1, 1] = 0.5 * X[k, 1]     
 
    return X[:,0], X[:,1]
        
if __name__ == '__main__':
    x, y = sierpins(1000000)
    plt.figure(figsize = (10, 10))
    plt.plot(x, y, '.', markersize = 0.2)
    plt.axis('equal')
    plt.axis('off')
    plt.show()
