class Game(object):
	# 游戏最高分 类属性
	top_score = 99

	# 显示帮助信息
	@staticmethod
	def show_help():
		print("欢迎来到王者峡谷")

	@classmethod
	def show_top_score(cls):
		print("最高分是："+str(cls.top_score))

	def __init__(self,name):
		# 玩家的名字
		self.player_name = name

	def start_game(self):
		print("开始游戏")


zhang_san = Game("张三")

Game.show_top_score()
Game.show_help()

 
