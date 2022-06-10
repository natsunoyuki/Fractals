import numpy as np
import matplotlib.pyplot as plt

class BarnsleyFern(object):
    def __init__(self, N = 10000, run = False):
        """
        Parameters
        -----
        N: int
            Number of points to generate.
        run: bool
            Flag to run the fractal generation functions.
        """
        self.N = N
        self.X = None

        if run == True:
            self.fern(N)
    
    def run(self):
        self.fern()

    def fern(self, N, return_X = False):
        """
        This function generates the barnsley fern fractal
        
        Input
        -----
        N: int
            Number of points to generate.
        return_X: bool
            Flag whether to return the points containing the fractal.
            
        Returns
        -------
        X: np.array
            2D points of the Barnsley fern fractal.
        """
        if N is None:
            N = self.N

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
        
        self.X = x.copy()

        if return_X == True:
            return self.X

    def plot(self, figsize = [10, 10], markersize = 0.2):
        assert self.X is not None
        x, y = self.X[:, 0], self.X[:, 1]
        plt.figure(figsize = figsize)
        plt.plot(x, y, 'g.', markersize = markersize)
        plt.axis('equal')
        plt.axis('off')
        plt.show()
