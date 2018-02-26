class Dog():

    # __init__ 叫初始化化方法 魔法方法（系统方法）
    def __init__(self,new_name):
        # 属性
        self.name = new_name
    
    def print_self_name(self):
        print(self.name)
    
    def print_self_color(self,color):
        return color


dog1 = Dog('张三')
dog1.print_self_name()
dog1.color = "yellow"
print(id(dog1))
print(dog1.color)
print(dog1.print_self_color('yellow'))
print("*"*20)
dog2 = Dog("李四")
dog2.print_self_name()
print(id(dog2))
