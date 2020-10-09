def func(a, b=5, c=10):
    '''hello,
    world'''
    print(a,b,c)

func(3,7)  #a=3,b=7,c=10
func(3,c=24)  #a=3, b=5, c=24   关键字参数
func(c=10,a=10) #a=10, b=5，c=10
print(func.__doc__)
dir(func)