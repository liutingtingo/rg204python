class Person(object):

    def __init__(self):
        self.name ="XXXX"

    def __del__(self):
        print("删除")

    def printLine(self):
        print("*"*20)

p = Person()

