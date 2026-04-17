import numpy as np
def NAND(x1,x2):
    a=np.array([x1,x2])
    b=np.array([-0.5,-0.5])
    o=0.7
    temp=np.sum(a*b)+o
    if temp>=0:
        return 1
    else:
        return 0
def AND(x1,x2):
    w1=0.5
    w2=0.5
    o=0.7
    temp=w1*x1+w2*x2
    if temp<=o:
        return 0
    else:
        return 1
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y