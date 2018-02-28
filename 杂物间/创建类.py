class Car():
	# 移动
	def move(self):
		print("车载奔跑")

	# 鸣笛
	def toot(self):
		print("车在鸣笛")

BWM = Car()
BWM.color = "黑色"
BWM.wheelNum = 4 #轮子数量

BWM.move()
BWM.toot()

print(BWM.color)
print(BWM.wheelNum)