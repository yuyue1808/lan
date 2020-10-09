#计算圆周率π
from random import random 
from math import sqrt
from time import clock
hits = 0 #用来四分之一圆形内落点个数
for i in range(1,DARTS) :
    x, y = random(), random()
    dist = sqrt(x**2 + y**2) 
    if dist <= 1.0 :
        hits = hits + 1
pai = (hits/DARTS) * 4 
print("pai的值是 %s" % pai)

