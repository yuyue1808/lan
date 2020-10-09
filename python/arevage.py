#求取平均值（通用式循环的运用）
'''
#交互式循环
def main() :
    sum = 0.0
    count = 0
    moredata = "y"
    while moredata =="y" :
        x = eval(input("Enter a number = "))
        sum = sum + x
        count = count + 1
        moredata = input("Do you have more numbers (yes or no) ?")
    print("\nThe average of the numbers is", sum / count)
main()
'''
'''
#哨兵循环
def main() :
    sum = 0.0
    count = 0
    moredata = input("Enter a number =")
    while moredata !="" :
        x = eval(moredata)
        sum = sum + x
        count = count + 1
        moredata = input("Enter a number =")
    print("\nThe average of the numbers is", sum / count)
main()
'''
'''
#文件循环
def main() :
    fileName = input("What is the filename?")
    infile = open(fileName, 'r')
    sum = 0
    count = 0
    line = infile.readline()
    while line != "" :
        sum = sum + eval(line)
        count = count + 1
        line = infile.readline()
    
    # for line in infile :
    #     sum = sum + eval(line)
    #     count = count + 1
        
    print("\nThe average of the numbers is", sum / count)
main()
'''
#嵌套循环
def main() :
    fileName = input("What is the filename?")
    infile = open(fileName, 'r')
    sum = 0
    count = 0
    line = infile.readline()
    while line != "" :
        for xstr in line.split(",") :
            sum = sum + eval(xstr)
            count = count + 1
        line = infile.readline()
    print("\nThe average of the numbers is", sum / count)
main()