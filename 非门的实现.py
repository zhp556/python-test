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
