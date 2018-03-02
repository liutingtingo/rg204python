class Aniaml(object):
	# 初始化方法
	def __init__(self):
		self.pin_zhong = "动物"

	# 这是方法（行为） 输出品种
	def print_name(self):
		print("绿叶给我初恋般的感觉")

class Dog(Aniaml):
	def pao(self):
		print("狗在跑")
	# 重写父类的方法
	def print_name(self):
		#super().print_name()
		print("红花")

	def cry(self):
		print("狗在哭")

class Cat(Aniaml):
	def miao(self):
		print("猫在喵")
	def cry(self):
		print("猫在哭")

# 继承的顺序 决定了我们继承的内容
class ZaJiao(Cat,Dog):
	pass


d = Dog()
d.print_name()


# 重写

# a = ZaJiao()
# a.cry()

# 实例化一个对象
# a = ZaJiao()
# a.pao()
# a.miao()
# a.pin_zhong ="猫狗兽"
# a.print_name()








# 这里是继承   狗类具有动物类的方法
# wanwan = Dog()
# wanwan.pin_zhong = "狗"
# wanwan.print_name()
# wanwan.pao()


# 实例化一个对象
# a = Aniaml()
# a.pin_zhong = "哈巴狗"
# a.print_name()
