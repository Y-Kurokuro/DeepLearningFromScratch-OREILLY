import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])  #入力
    w = np.array([0.5, 0.5])    #重み
    b = -0.7    #バイアス

    tmp = np.sum(w*x) + b   #ANDゲート本体
    if tmp <= 0:
        return 0
    else:
        return 1

print(AND(0, 0))
print(AND(1, 0))
print(AND(0, 1))
print(AND(1, 1))