#文件拷贝
def main() :
    #用户输入文件名
    f1 = input("Enter the file :").strip()
    f2 = input("Enter the outfile :").strip()
    #打开文件
    file = open(f1, "r")
    outfile = open(f2, "w")
    #拷贝操作
    countlines = countchars = 0
    for line in file :
        countlines += 1
        countchars += len(line)
        outfile.write(line)
    print(countlines, "lines and", countchars, "chars copied")
    
    file.close()
    outfile.close()
    
main()