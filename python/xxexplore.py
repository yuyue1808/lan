#用于一元二次方程求解（if-else)
from math import *
def main() :
    a, b, c = eval(input("Please input the (a, b, c) ="))#这个eval有什么用
    delta = b**2 - 4 * a * c
    if a == 0 :
        root = - c / b
        print("\nThe only root is ", root)
    else :   
        if delta > 0 :
          root1 = (-b + sqrt(delta)) / (2 * a)
          root2 = (-b - sqrt(delta)) / (2 * a)
          print("\nThe two roots are ", root1, root2)
        elif delta == 0:
            root = (-b ) / (2 * a)
            print("\nThe only root is ", root)
        else :
          print("these are no real roots!")

main()        
        
    