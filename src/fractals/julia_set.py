import numpy as np
import matplotlib.pyplot as plt

class JuliaSet(object):
    def __init__(self, c = -0.835 - 0.2321 * 1j, num_iter = 50, N = 1000, X0 = np.array([-2, 2, -2, 2]), run = False):
        """
        Generates the Julia set fractal
        
        Inputs
        ------
        num_iter: int
            number of iterations to run
        N: int
            number of grid points on each axis to use. We use a square grid
        X0: np.array
            bounding box of the square grid to use
        run: bool
            Flag to run the fractal generation functions.
        """
        self.c = c
        self.num_iter = num_iter
        self.N = N
        self.X0 = X0

        if run == True:
            self.julia_set(c, num_iter, N, X0, False)

    def run(self):
        self.julia_set()

    def julia_set(self, c = None, num_iter = None, N = None, X0 = None, return_X = False):
        """
        Generates the Julia set fractal
        
        Inputs
        ------
        num_iter: int
            number of iterations to run
        N: int
            number of grid points on each axis to use. We use a square grid
        X0: np.array
            bounding box of the square grid to use
        return_X: bool
            flag indicating whether to return the generated results
        
        Returns
        -------
        x: np.array
            x axis vlaues
        y: np.array
            y axis values
        F: np.array
            2D np.array containing the fractal
        """
        if c is None:
            c = self.c
        if num_iter is None:
            num_iter = self.num_iter
        if N is None:
            N = self.N
        if X0 is None:
            X0 = self.X0

        x0 = X0[0]
        x1 = X0[1]
        y0 = X0[2]
        y1 = X0[3]
        
        # Set up the complex grid z = x + yi
        x, y = np.meshgrid(np.linspace(x0, x1, N), np.linspace(y0, y1, N) * 1j)
        z = x + y
        
        # F keeps track of which grid points are bounded
        # even after many iterations of z_n+1 = z_n**2 + c.
        F = np.zeros([N, N])
        
        for j in range(num_iter):
            z = z ** 2 + c
            index = np.abs(z) < np.inf
            F[index] = F[index] + 1

        self.x = np.linspace(x0,x1,N)
        self.y = np.linspace(y0,y1,N)
        self.F = F

        if return_X == True:
            return self.x, self.y, self.F
     
    def plot(self, figsize = [10, 10]):
        plt.figure(figsize = figsize)
        plt.pcolormesh(self.x, self.y, self.F, cmap = 'binary')
        plt.axis('equal')
        plt.axis('off')
        plt.show()