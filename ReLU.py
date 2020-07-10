import numpy as np
import matplotlib.pylab as plt

def relu(x):   #x > 0ならば1、それ以外は0を返す
    return np.maximum(0, x)

x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show