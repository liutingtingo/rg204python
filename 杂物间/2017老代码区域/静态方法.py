class Dog(object):
	__count = 0
	def __init__(self):
		pass

	def test2(self):
		pass

	@classmethod
	def test(cls,num):
		
		cls.count = num
		print("这是一个类方法")

	# 静态方法就是 既不需要调用类方法 也不需要调用实例方法的时候使用
	@staticmethod
	def run():
		print("狗在跑")


def run2():
	print("猫在叫")


Dog.run()

Dog.count = 5
Dog.test(5)