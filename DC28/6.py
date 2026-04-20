#Wap to create setter and getter methods for a variable
class Student:
    def __init__(self,name):
        self.__name = name #Private variable
        
    def setname(self,name):
        self.__name = name
        
    def getname(self):
        return self.__name
        
s1 = Student("nitin")

s1.setname("nitin")
print(s1.getname())


        
    