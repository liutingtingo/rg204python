# init方法
class Car():
	def __init__(self,a,b):
		self.wheelNum = a
		self.color = b

	def __str__(self):
		msg = "你好，车辆已经制造完毕，车的颜色是："+self.color+",一共"+str(self.wheelNum)+"个轮子"
		return msg

	def move(self):
		print("车在跑，目标：台湾")

# 创建对象
msld = Car("6", "green")


