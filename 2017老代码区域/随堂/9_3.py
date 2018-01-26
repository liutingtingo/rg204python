class User(object):
    
    def __init__(self):
        self.__first_name = ""
        self.__last_name = ""
        self.__addr = ""
        login_attempt = 0

    def getFirst_name(self):
        return self.__first_name

    def getLast_name(self):
        return self.__last_name

    def getAddr(self):
        return self.__addr
    
    def setFirst_name(self,new_first_name):
        self.__first_name = new_first_name 
        return self.__first_name

    def setLast_name(self,new_last_name):
        self.__last_name = new_last_name
        return self.__last_name

    def setAddr(self,new_addr):
        self.__addr = new_addr
        return self.__addr

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)

    def greet_user(self):
        print("%s%s说：你好！"%(self.__first_name,self.__last_name))
    
    def incriment_login_attempt(self):
        self.login_attempt += 1
    
    def reset_login_attempt(self):
        self.login_attempt = 0

u1 = User()

u1.setFirst_name("张")
u1.setLast_name("三")
u1.setAddr("泰国")

u1.greet_user()



print("_____________华丽分割线_________________")


u2 = User()
u2.setFirst_name("段劲松")
u2.setLast_name("段")
u2.setAddr("泰国曼谷")

u2.greet_user()

