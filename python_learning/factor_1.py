# import math 
# i = math.factorial(100)
# print(i)

def factor(i):
    if(i==1):
        return 1   
    else:
        return i*factor(i-1)

print(factor(3))
    