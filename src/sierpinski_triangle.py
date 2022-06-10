import numpy as np
import matplotlib.pyplot as plt

class SierpinskiTriangle(object):
    def __init__(self, N = 100000, run = False):
        """
        This function generates the Sierpinski triangle fractal.
        
        Input
        -----
        N: int
            Number of points to generate.
        run: bool
            Flag to run the fractal generation functions.
        """
        self.N = N

        if run == True:
            self.sierpinski_triangle(N)

    def run(self):
        self.sierpinski_triangle()

    def sierpinski_triangle(self, N = None, return_X = False):
        """
        This function generates the sierpinski triangle fractal
        
        Input
        -----
        N: int
            number of points to generate
        return_X: bool
                Flag to output the array containing the fractal.
            
        Returns
        -------
        X: np.array
            np.array of points of the cantor box
        """    
        if N is None:
            N = self.N

        X = np.zeros([N + 1, 2])

        for k in range(N):
            r = np.random.random()
            if r <= 1.0 / 3.0:
                X[k + 1, 0] = 0.5 * X[k, 0]
                X[k + 1, 1] = 0.5 * X[k, 1]
            elif r <= 2.0 / 3.0:
                X[k + 1, 0] = 0.5 * X[k, 0] + 0.25
                X[k + 1, 1] = 0.5 * X[k, 1] + np.sqrt(3) / 4.0
            else:
                X[k + 1, 0] = 0.5 * X[k, 0] + 0.5
                X[k + 1, 1] = 0.5 * X[k, 1]     
    
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
