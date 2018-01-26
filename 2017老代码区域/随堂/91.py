class Restaurant:

    def __init__(self):
        self.restaurant_name = "王润泽的奶茶店"
        self.cuisine = ['草莓奶茶','红豆奶茶','相遇奶茶','白色的稠稠的奶']
        self.__number_served = 0
    
    def setNumber_served(self,a):
        self.__number_served = a
        return self.__number_served

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine)

    def open_restaurant(self):
        print("%s在营业"%self.restaurant_name)

    def addPerson(self,n):
        self.__number_served += n
        print ('王润泽服务过的人数:',self.__number_served)

r1 = Restaurant()
print(r1.restaurant_name)
print(r1.cuisine)
r1.describe_restaurant()
r1.open_restaurant()

print("_____________华丽的分割线____________")

r1.setNumber_served(10)

print("_________华丽的分割线_________________")

r1.addPerson(3)

print("_________华丽的分割线_________________")
r1.addPerson(5)

