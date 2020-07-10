import numpy as np

def OR(x1, x2):
    x = np.array([x1, x2])  #入力
    w = np.array([0.5, 0.5])    #重み
    b = -0.2    #バイアスのみがANDと異なる(値が小さいので発火しやすい.よってどちらかが1ならば発火するORゲートになる.)

    tmp = np.sum(w*x) + b   #ORゲート本体
    if tmp <= 0:
        return 0
    else:
        return 1

print(OR(0, 0))
print(OR(1, 0))
print(OR(0, 1))
print(OR(1, 1))