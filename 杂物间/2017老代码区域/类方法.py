class Car(object):
	# # 类属性
	# Count = 10

	# 类方法
	@classmethod
	def move(cls):
		print("车在移动")

	# 静态方法
	@staticmethod
	def benpao():
		print("车在奔跑")

	def __init__(self):
		# 实例属性（对象属性） 属性
		self.color = "黄色"
	# def __del__(self):
	# 	Car.Count = Car.Count-1


Car.benpao()

a = Car()
a.benpao()

b= Car()
b.benpao()


#print(Car.Count)
# Car.move()