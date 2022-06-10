import numpy as np
import matplotlib.pyplot as plt

class MandelbrotSet(object):
    def __init__(self, num_iter = 50, N = 1000, X0 = np.array([-2, 1, -1.5, 1.5]), run = False):
        """
        Generates the Mandelbrot set fractal
        
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
        self.num_iter = num_iter
        self.N = N
        self.X0 = X0

        if run == True:
            self.mandelbrot_set(num_iter, N, X0)

    def run(self):
        self.mandelbrot_set()

    def mandelbrot_set(self, num_iter = 50, N = 1000, X0 = np.array([-2, 1, -1.5, 1.5]), return_X = False):
        """
        Generates the Mandelbrot set fractal
        
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
        x0 = X0[0]
        x1 = X0[1]
        y0 = X0[2]
        y1 = X0[3]
        i = 1j
        
        x, y = np.meshgrid(np.linspace(x0, x1, N), np.linspace(y0, y1, N) * i)
        z = x + y
        c = x + y
        F = np.zeros([N, N])
        
        for j in range(num_iter):
            z = z ** 2 + c 
            index = np.abs(z) < np.inf
            F[index] = F[index] + 1

        self.x = np.linspace(x0, x1, N)
        self.y = np.linspace(y0, y1, N)
        self.F = F

        if return_X == True:
            return self.x, self.y, self.F

    def plot(self, figsize = [10, 10]):
        plt.figure(figsize = figsize)
        plt.pcolormesh(self.x, self.y, self.F, cmap = 'binary')
        plt.axis('equal')
        plt.axis('off')
        plt.show()
