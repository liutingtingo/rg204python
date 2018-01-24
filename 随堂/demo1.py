class Car(object):

    def __init__(self,newcolor,newpp):
        self.color = newcolor
        self.pp = newpp
    
    def __str__(self):
        return self.color

    def move(self):
        print("那辆颜色为%s的车在移动"%self.color)


lbjn = Car('blue','兰博基尼')

print(lbjn)







#class Dog:
#    pass
#
#
## 对象 实例
#bmw = Car('white','宝马')
#
#isCar = isinstance(bmw,Car)
#print('*'*5,isCar,'*'*5)
#
#bc = Dog()
#
#isCar = isinstance(bc,Car)
#print(isCar)
#

#blue_car = Car('blue')
#blue_car.color = 'red'
#blue_car.move()
#
#yellow_car = Car('yellow')
#yellow_car.move()




