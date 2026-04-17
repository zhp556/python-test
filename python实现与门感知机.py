def AND(x1,x2):
    w1=0.5
    w2=0.5
    o=0.7
    temp=w1*x1+w2*x2
    if temp<=o:
        return 0
    else:
        return 1
print(AND(0,0))