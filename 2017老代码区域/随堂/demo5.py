class Animal(object):
    def __init__(self):
        self.name = "段金松"
        self.__man = "NO"

    def cry(self):
        print("%s在哭"%self.name)

    def isMan(self):
        print("是不是man:%s"%self.__man)


class Dog(Animal):
    
    def wan(self):
        print("%s:旺旺旺"%self.name)

    def isMan2(self):
        print(self.__man)

alsj = Dog()
alsj.wan()
alsj.cry()
alsj.isMan()
print("-----------华丽分割线________")
#alsj.isMan2()

