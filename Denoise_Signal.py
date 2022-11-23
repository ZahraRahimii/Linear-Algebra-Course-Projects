import numpy as np
import matplotlib.pyplot as plt
import math

lambda1 = 10

def least_square1(y, n ):
    D = np.zeros((n - 1, n), dtype=float)
    for i in range(0, n-1):
        D[i, i+1] = -1 * math.sqrt(lambda1)
        D[i, i] = 1 * math.sqrt(lambda1)
    I = np.eye(n, n)
    A = np.vstack((I, D))
    yy = np.asarray(y)
    b = np.vstack((yy.reshape(-1,1), np.zeros((n, 1), dtype=float) ))
    AT = np.transpose(A)
    ATA = np.dot(AT, A)
    ATb = np.dot(AT, b)

    return np.linalg.solve(ATA, ATb)



path = "btc_price.npy"
path2 = "s.npy"
y = np.load(path, mmap_mode='r')
x = least_square1(y, 2501)

plt.plot(y)
plt.plot(x)

plt.show()


# n = 10
# least_square(n)
