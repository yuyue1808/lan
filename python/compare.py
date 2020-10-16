class student(object):#数据封装
    def __init__ (self, name, hours, points) :
        self.name = name
        self.hours = float(hours)
        self.points = float(points)
    def gpa(self) :
        return self.points/self.hours
    
def makestudent(str1) :
    name, hours, points = str1.split("\t")
    return student(name, hours, points)

def main() :
    filename0 = input("Please input the filename:")
    in_file = open(filename0,'r')
    
    best = makestudent(in_file.readline())
    
    for line in in_file :
        s = makestudent(line)
        if s.gpa() > best.gpa() :
                best = s
        else :
                continue
    in_file.close()
    
    print("THE BEST STUDENT'S NAME IS ")
    print("the hours=", best.hours)   

main()
            