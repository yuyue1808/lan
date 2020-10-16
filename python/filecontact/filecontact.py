#实现电话簿与邮箱簿的整合
def main() :
    #打开两个文件
    telefile = open('telebook.txt', 'rb')
    emailfile = open('emailbook.txt', 'rb')
    
    telefile.readline()
    emailfile.readline()#跳过第一行  
    lines1 = telefile.readlines()
    lines2 = emailfile.readlines()#将文件读成一个列表
    
    #创建暂时存储列表
    list1_name = []
    list1_tele = []
    list2_name = []
    list2_email = []  
    
    #获取第一个文本里的姓名和电话(读出解码)
    for line in lines1 :
        element = line.split()
        list1_name.append(str(element[0].decode('gbk')))
        list1_tele.append(str(element[1].decode('gbk')))
      
    #获取第二个文本里的姓名和电话
    for line in lines2 :
        element = line.split()
        list2_name.append(str(element[0].decode('gbk')))
        list2_email.append(str(element[1].decode('gbk')))  
    
    #开始处理
    list3 = []
    list3.append('姓名\t电话\t    邮箱\n')
    
    #按索引方法遍历名字列表1
    for i in range(len(list1_name)):
        s = ''
        if list1_name[i] in list2_name :
            j = list2_name.index(list1_name[i])
            s = '\t'.join([list1_name[i], list1_tele[i], list2_email[j]])
        else:
            s = '\t'.join([list1_name[i], list1_tele[i], str('------')])
        s += '\n'
        list3.append(s)

    #处理遍历列表2的剩余部分
    for i in range(len(list2_name)):
        s = ''
        if list2_name[i] not in list1_name :
            s = '\t'.join([list2_name[i], str('------'), list2_email[i]])
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
    
            