import numpy as np
import matplotlib.pyplot as plt

def weierstrauss_fractal(x0 = -1, x1 = 1, Nx = 2000, a = 0.5, n_iter = 20):
    x = np.linspace(x0, x1, Nx)
    f = np.zeros(len(x))
    b = int((1 + 3 / 2 * np.pi) / a + 1)
    
    for i in range(n_iter):
        f = f + a ** i * np.cos(b ** i * np.pi * x)
    
    return x, f
    
if __name__ == '__main__':
    x, f = weierstrauss_fractal()
    plt.figure(figsize=(10, 5))
    plt.plot(x, f)
    plt.show()