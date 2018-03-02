class A(object):
	def __init__(self):
		print("这是init方法")
		
	# __new__至少要由一个参数cls,代表要实例化的类
	def __new__(cls):
		print("这是new方法")
		return object.__new__(cls)

A()