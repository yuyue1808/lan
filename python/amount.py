#计算汇率（递归的使用）
'''    #为每年绘制星号的增长图
def createTable(principal, apr) :
    for year in range(1,  11) :
        principal = principal * (1 + apr)
        print("%2d"%year, end = '')
        total = calculateNum(principal)
        print("*" * total)
    print(" 0.0k   2.5k   5.0k   7.5k   10.0k")
def calculateNum(principal) :
    #计算星号数量
    total = int(principal * 4 / 1000.0)
    return total
def main() :
    print("This program plots the growth of a 10-year investment.")
    #输入本金和汇率
    principal = eval(input("Enter the initial principal :"))
    apr = eval(input("Enter the annualized interest rate:"))
    #建立图表
    createTable(principal, apr)
main()
'''

#字符串翻转
def reverse(s) :
    if s == "" :
        return s
    else:
        return reverse(s[1:]) + s[0]
def main() :
    str1 = input("please input the s:")
    str2 = reverse(str1)
    print("the result=", str2)
main()