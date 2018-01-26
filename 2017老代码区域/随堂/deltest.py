class Dog(object):

    def __init__(self):
        self.name = "XXX"

    def __del__(self):
        print("对象被删除了")

    #def __str__(self):
    #    return "调用str"
    
    def printLine(self):
        print("*"*20)

alsj = Dog()
#print(alsj)
del alsj
alsj.printLine()




