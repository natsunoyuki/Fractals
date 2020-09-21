import numpy as np
import matplotlib.pyplot as plt

def cantor_box(N):
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
        
    return X[:,0],X[:,1]

if __name__ == '__main__':   
    x, y = cantor_box(200000)
    plt.figure(figsize = (8, 8))
    plt.plot(x, y, '.', markersize = 0.2)
    plt.axis('equal')
    plt.axis('off')
    plt.show()