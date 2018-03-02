class Tool(object):
	# 使用赋值语句定义类属性，记录创建工具对象的总数
	count = 0

	def __init__(self,name):
		self.name = name

		# 让类属性的值+1
		Tool.count += 1

	@classmethod
	def tool_show_count(cls):
		print("创建了%d"%Tool.count)
		print("创建了%d"%cls.count)

# 1.创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")

Tool.tool_show_count()

# 2.输出工具对象的总数
# print(Tool.count)

# tool1.count = 4

# print(Tool.count)
# print(tool1.count)
# print(tool2.count)






