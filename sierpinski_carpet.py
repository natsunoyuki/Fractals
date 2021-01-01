import numpy as np
import matplotlib.pyplot as plt

def sierpinski_carpet(N):
    """
    This function generates the Sierpinski carpet fractal.
    Note that the Sierpinski triangle fractal is a related
    but different fractal.
    
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
        r = np.random.random()
        if r <= 1.0/8.0:
            X[k+1, 0] = 1.0/3.0 * X[k, 0]
            X[k+1, 1] = 1.0/3.0 * X[k, 1]
        elif r <= 2.0/8.0:
            X[k+1, 0] = 1.0/3.0 * X[k, 0] + 1.0/3.0
            X[k+1, 1] = 1.0/3.0 * X[k, 1]
        elif r <= 3.0/8.0:
            X[k+1, 0] = 1.0/3.0 * X[k, 0] + 2.0/3.0
            X[k+1, 1] = 1.0/3.0 * X[k, 1]
        elif r <= 4.0/8.0:
            X[k+1, 0] = 1.0/3.0 * X[k, 0]
            X[k+1, 1] = 1.0/3.0 * X[k, 1] + 1.0/3.0
        elif r <= 5.0/8.0:
            X[k+1, 0] = 1.0/3.0 * X[k, 0] + 2.0/3.0
            X[k+1, 1] = 1.0/3.0 * X[k, 1] + 1.0/3.0
        elif r <= 6.0/8.0:
            X[k+1, 0] = 1.0/3.0 * X[k, 0] 
            X[k+1, 1] = 1.0/3.0 * X[k, 1] + 2.0/3.0
        elif r <= 7.0/8.0:
            X[k+1, 0] = 1.0/3.0 * X[k, 0] + 1.0/3.0
            X[k+1, 1] = 1.0/3.0 * X[k, 1] + 2.0/3.0
        else:
            X[k+1, 0] = 1.0/3.0 * X[k, 0] + 2.0/3.0
            X[k+1, 1] = 1.0/3.0 * X[k, 1] + 2.0/3.0

    return X[:,0], X[:,1]
        
if __name__ == '__main__':
    x, y = sierpinski_carpet(1000000)
    plt.figure(figsize = (10, 10))
    plt.plot(x, y, '.', markersize = 0.2)
    plt.axis('equal')
    plt.axis('off')
    plt.show()