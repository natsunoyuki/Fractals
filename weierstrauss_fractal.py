import numpy as np
import matplotlib.pyplot as plt

def weierstrauss_fractal(x0 = -1, x1 = 1, Nx = 10000, a = 0.5, n_iter = 20):
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
    
    return x, f
    
if __name__ == '__main__':
    x, f = weierstrauss_fractal()
    plt.figure(figsize=(15, 5))
    plt.plot(x, f)
    plt.grid(True)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()
