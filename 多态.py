class Dog(object):

	def __init__(self,name):
		self.name = name

	def game(self):
		print(self.name+"蹦蹦跳跳的玩耍...")

class XiaoTianDog(Dog):

	def game(self):
		print(self.name+"飞到天上去玩耍")

class Person(object):

	def __init__(self,name):
		self.name = name

	def game_with_dog(self,dog):
		print("%s和%s快乐的玩耍..."%(self.name,dog.name))
		# 让狗玩耍
		dog.game()


# 创建一个狗对象
#wancai = Dog("旺财")
feitianwancai = XiaoTianDog("飞天旺财")


# 创建一个小明对象
xiaoming = Person("小明")

# 让小明调用和狗玩的方法
xiaoming.game_with_dog(feitianwancai)


