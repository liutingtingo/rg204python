class People(object):
    
    def __init__(self,name):
        # __为私有属性（保护属性）
        self.__name = name
        self.__age = 0

    def setAge(self,newAge):
        self.__age = newAge
        

    def getAge(self):
        return self.__age

    def setName(self,newname):
        self.__name = newname
    
    def getName(self):
        print(self.__name)

whq = People("王含青")

#print(whq.__name)
#whq.__name = "段劲松"
#print(whq.__name)
#whq.print_name()

