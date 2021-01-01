import numpy as np
import matplotlib.pyplot as plt

def fern(N):
    """
    This function generates the barnsley fern fractal
    
    Input
    -----
    N: int
        number of points to generate
        
    Returns
    -------
    X: np.array
        np.array of points of the cantor box
    """
    x = np.zeros([N + 1, 2])
    x[0, :] = np.array([0.5, 0.5])
    for k in range(N):
        r = np.random.random()
        if r <= 0.01:
            x[k + 1, 0] = 0
            x[k + 1, 1] = 0.16 * x[k, 1]
        elif r <= 0.85:
            x[k + 1, 0] = 0.85 * x[k, 0] + 0.04 * x[k, 1]
            x[k + 1, 1] = -0.04 * x[k, 0] + 0.85 * x[k, 1] + 1.6
        elif r <= 0.93:
            x[k + 1, 0] = 0.2 * x[k, 0] - 0.26 * x[k, 1]
            x[k + 1, 1] = 0.23 * x[k, 0] + 0.22 * x[k, 1] + 1.6
        else:
            x[k + 1, 0] = -0.15 * x[k, 0] + 0.28 * x[k, 1] + 0.26
            x[k + 1, 1] = 0.26 * x[k, 0] + 0.24 * x[k, 1] + 0.44
    
    return x[:,0], x[:,1]

if __name__ == '__main__':
    x, y = fern(200000)
    plt.figure(figsize = (10, 10))
    plt.plot(x, y, 'g.', markersize = 0.2)
    plt.axis('equal')
    plt.axis('off')
    plt.show()
