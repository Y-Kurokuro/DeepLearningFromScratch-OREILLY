import numpy as np
import matplotlib.pylab as plt

def step_function(x):   #x > 0ならば1、それ以外は0を返す
    return np.array(x > 0, dtype = np.int)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show