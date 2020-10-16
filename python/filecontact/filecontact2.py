#实现电话簿与邮箱簿的整合
def main() :
    #打开两个文件
    telefile = open('telebook.txt', 'rb')
    emailfile = open('emailbook.txt', 'rb')
    
    telefile.readline()
    emailfile.readline()#跳过第一行  
    lines1 = telefile.readlines()
    lines2 = emailfile.readlines()#将文件读成一个列表
    
    #创建暂时存储字典
    list1 = {}
    list2 = {}  
    
    #获取第一个文本里的姓名和电话(读出解码)
    for line in lines1 :
        element = line.split()
        list1[str(element[0].decode('gbk'))] = str(element[1].decode('gbk'))
       
    #获取第二个文本里的姓名和电话
    for line in lines2 :
        element = line.split()
        list2[str(element[0].decode('gbk'))] = str(element[1].decode('gbk'))
    print(list1)
    print('\n')
   
    #开始处理
    list3 = []
    list3.append('姓名\t电话\t    邮箱\n')
    
    #按索引方法遍历名字列表1
    for key in list1:
        s = ''
        if key in list2 :
            s = '\t'.join([key, list1[key], list2[key]])
        else:
            s = '\t'.join([key, list1[key], str('------')])
        s += '\n'
        list3.append(s)

    #处理遍历列表2的剩余部分
    for key in list2:
        s = ''
        if key not in list1 :
            s = '\t'.join([key, str('------'), list2[key]])
            s += '\n'
        list3.append(s)
        
    #把列表3读入文件中
    file = open("book.txt", 'w')
    file.writelines(list3)
    file.close()
    
    telefile.close()
    emailfile.close()
    print("have finished")
    
main()
    
            