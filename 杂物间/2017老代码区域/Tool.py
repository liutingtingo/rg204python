class Tool(object):
	count = 0;
	def __init__(self,name):
		self.name = name
		Tool.count += 1

gai_zui = Tool("改锥")
luo_si_dao = Tool("螺丝刀")

#print(Tool.count)
print(gai_zui.count)
print(luo_si_dao.count)