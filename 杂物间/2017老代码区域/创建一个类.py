class Person(object):
	# 这是一个魔法方法，在这个方法里面去定义对象属性
	def __init__(self,eye_color):
		self.eye_color = eye_color
	# 这个是 输出定制内容   如果不设置这个方法则输出内存地址
	def __str__(self):
		return "我爱你"

	def __del__(self):
		print("对象销毁了")

	# 这是对象方法
	def walk(self,name):
		print(name+"在走")

print("1")
z_q_y = Person("green")
del z_q_y
print("2")

print("程序结束了")





# print(Person("red"))
# print("*"*20)
# duan_jin_song = Person("white")
# duan_jin_song.walk("段劲松")
# f_x_m = Person("blue")

# print(id(duan_jin_song))
# print("*"*20)
# print(id(f_x_m))




