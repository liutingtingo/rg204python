import pygame
from plane_sprites import *

class PlaneGame(object):
	"""飞机大战主游戏"""

	def __init__(self):
		print("游戏初始化")
		# 1 创建游戏窗口
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		# 2 创建游戏时钟
		self.clock = pygame.time.Clock()
		# 3 调用精灵和精灵组（我设置成私有方法）
		self.__create_sprites()
		# 4 设置定时器事件 每秒钟创建一家敌机
		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)

	def start_game(self):
		print("开始游戏")
		while True:
			# 1、设置刷新帧率
			self.clock.tick(60)
			# 2、事件监听
			self.__event_handler()
			# 3、碰撞检测
			self.__check_collide()
			# 4、更新精灵组
			self.__update_sprites()
			# 5、更新屏幕显示
			pygame.display.update()
		


	def __event_handler(self):
		"""事件监听"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				PlaneGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:
				print("敌机出场")
				self.enemy_group.add(Enemy())

	def __check_collide(self):
		"""碰撞检测"""
		pass

	
			

	@staticmethod
	def __game_over():
		"""游戏结束"""
		print("游戏结束")
		# 卸载模块
		pygame.quit()
		# 退出Python脚本
		exit()

	def __create_sprites(self):
		"""创建精灵和精灵组"""
		bg1 = Background()
		bg2 = Background(True)
		bg2.rect.y = -bg2.rect.height
		# 背景组
		self.back_group = pygame.sprite.Group(bg1,bg2)
		# 敌机组
		self.enemy_group = pygame.sprite.Group()
		# 英雄组
		self.hero_group = pygame.sprite.Group()
	def __update_sprites(self):
		"""更新精灵和精灵组"""
		for group in [self.back_group,self.enemy_group,self.hero_group]:
			group.update()
			group.draw(self.screen)



if __name__ == "__main__":
	# 使用游戏类  创建一个游戏对象
	game = PlaneGame()
	# 开始游戏
	game.start_game() 