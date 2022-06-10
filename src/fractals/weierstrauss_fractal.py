import numpy as np
import matplotlib.pyplot as plt

class WeierstraussFractal(object):
    def __init__(self, x0 = -1, x1 = 1, Nx = 10000, a = 0.5, n_iter = 20, run = False):
        """
        Generate the weierstrauss fractal
        
        Inputs
        ------
        x0: float
            start point of the x axis
        x1: float
            end point of the x axis
        Nx: int
            number of points to use along the x axis
        a: float
            weierstrauss fractal factor
        n_iter: int
            number of iterations to run
        run: bool
            Flag to run the fractal generation functions.
        """
        self.x0 = x0
        self.x1 = x1
        self.Nx = Nx
        self.a = a
        self.n_iter = n_iter

        if run == True:
            self.weierstrauss_fractal(x0, x1, Nx, a, n_iter)

    def run(self):
        self.weierstrauss_fractal()

    def weierstrauss_fractal(self, x0 = -1, x1 = 1, Nx = 10000, a = 0.5, n_iter = 20, return_X = False):
        """
        Generate the weierstrauss fractal
        
        Inputs
        ------
        x0: float
            start point of the x axis
        x1: float
            end point of the x axis
        Nx: int
            number of points to use along the x axis
        a: float
            weierstrauss fractal factor
        n_iter: int
            number of iterations to run
        return_X: bool
                Flag to output the array containing the fractal.
            
        Returns
        -------
        x: np.array
            x axis values
        f: np.array
            f(x) containing the fractal
        """
        x = np.linspace(x0, x1, Nx)
        f = np.zeros(len(x))
        b = int((1 + 3 / 2 * np.pi) / a + 1)
        
        for i in range(n_iter):
            f = f + a ** i * np.cos(b ** i * np.pi * x)
        
        self.x = x
        self.f = f
        if return_X == True:
            return x, f

    def plot(self, figsize = [10, 5]):
        plt.figure(figsize = figsize)
        plt.plot(self.x, self.f)
        plt.show()