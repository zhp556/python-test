import matplotlib.pyplot as plt
import numpy as np
def jump_f(a):                #这个函数只能接受实数即浮点数的输入，因此下面进行了改版
    if a>0:
        return 1
    else:
        return 0

def step_function(x):         #这个函数中y.astype(np.int)是把y转变为int型
    y = x > 0                 #这里与c语言不同的是将y进行了一个布尔值的赋值，取决于后面的x相对于0的大小
    return y.astype(int)      #书上的这里写的是np.int，但新版numpy已经废弃了这个用法，应该是int
                              #尤其是当x是numpy数组的时候，y将变成将x中每一个数变成布尔值的numpy数组，演示如下
                              #>>> import numpy as np
                              #>>> x = np.array([-1.0, 1.0, 2.0])
                              #>>> x
                              #array([-1.,  1.,  2.])
                              #>>> y = x > 0
                              #>>> y
                              #array([False,  True,  True], dtype=bool)
def step_function2(x):
    return np.array(x>0,dtype=int)
x=np.arange(-5,5,0.1)
y=step_function2(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()

