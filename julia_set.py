import numpy as np
import matplotlib.pyplot as plt

def julia_set(num_iter = 50, N = 1000, X0 = np.array([-2, 2, -2, 2])):
    x0 = X0[0]
    x1 = X0[1]
    y0 = X0[2]
    y1 = X0[3]
    i = 1j
    
    x, y = np.meshgrid(np.linspace(x0, x1, N), np.linspace(y0, y1, N) * i)
    z = x + y
    F = np.zeros([N, N])
    
    for j in range(num_iter):
        index = np.abs(z) < np.inf
        F[index] = F[index] + 1
        z = z ** 2 + -0.835 - 0.2321 * i

    return np.linspace(x0,x1,N), np.linspace(y0,y1,N), F
    
if __name__ == '__main__':
    x, y, F = julia_set()
    plt.figure(figsize = (8, 8))
    plt.pcolormesh(x, y, F, cmap = 'binary')
    plt.axis('equal')
    plt.axis('off')
    plt.show()