import numpy as np
import matplotlib.pyplot as plt

class CantorBox(object):
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
            self.cantor_box(N)

    def run(self):
        self.cantor_box()

    def cantor_box(self, N = None, return_X = False):
        """
        This function generates the cantor box fractal
        
        Input
        -----
        N: int
            Number of points to generate.
        return_X: bool
            Flag to output the array containing the fractal.
            
        Returns
        -------
        X: np.array
            2D points of the cantor box.
        """
        if N is None:
            N = self.N

        X = np.zeros([N + 1, 2])

        for k in range(N):
            r = np.random.random()
            if r <= 1. / 8:
                X[k + 1, 0] = 1. / 9 * X[k, 0]
                X[k + 1, 1] = 1. / 9 * X[k, 1]
            elif r <= 2. / 8:
                X[k + 1, 0] = 1. / 9 * X[k, 0] + 1. / 3
                X[k + 1, 1] = 1. / 9 * X[k, 1]
            elif r <= 3. / 8:
                X[k + 1, 0] = 1. / 9 * X[k, 0] + 2. / 3
                X[k + 1, 1] = 1. / 9 * X[k, 1]
            elif r <= 4. / 8:
                X[k + 1, 0] = 1. / 9 * X[k, 0]
                X[k + 1, 1] = 1. / 9 * X[k, 1] + 1. / 3
            elif r <= 5. / 8:
                X[k + 1, 0] = 1. / 9 * X[k, 0]
                X[k + 1, 1] = 1. / 9 * X[k, 1] + 2. / 3
            elif r <= 6. / 8:
                X[k + 1, 0] = 1. / 9 * X[k, 0] + 1. / 3
                X[k + 1, 1] = 1. / 9 * X[k, 1] + 2. / 3
            elif r <= 7. / 8:
                X[k + 1, 0] = 1. / 9 * X[k, 0] + 2. / 3
                X[k + 1, 1] = 1. / 9 * X[k, 1] + 2. / 3
            else:
                X[k + 1, 0] = 1. / 9 * X[k, 0] + 2. / 3
                X[k + 1, 1] = 1. / 9 * X[k, 1] + 1. / 3

        self.X = X.copy()    
        
        if return_X == True:
            return self.X

    def plot(self, figsize = [10, 10], markersize = 0.2):
        assert self.X is not None
        x, y = self.X[:, 0], self.X[:, 1]
        plt.figure(figsize = figsize)
        plt.plot(x, y, '.', markersize = markersize)
        plt.axis('equal')
        plt.axis('off')
        plt.show()
