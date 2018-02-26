class Restaurant(object):
    """这是一个餐馆类"""
    def __init__(self):
        
        # 餐馆的名字
        self.restaurant_name = "段金松的小店"
        # 菜品
        self.cuisine = "人肉包子"

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine)

    def open_restaurant(self):
        print("%s___正在营业"%self.restaurant_name)

r1 = Restaurant()
#调用属性
a1 = r1.restaurant_name
b1 = r1.cuisine
#调用方法
r1.describe_restaurant()

r2 = Restaurant()
r2.restaurant_name = "冯新明的小铺"
r2.cuisine = "猪肉包子"
r2.describe_restaurant()

r3 = Restaurant()
r3.cuisine = "龙肉包子"
r3.restaurant_name = "庞源怂的"
r3.describe_restaurant()


