import pygame
from plane_sprites import *
# import plane_sprites

class PlaneGame(object):

	def __init__(self):
		"""
		1 游戏窗口
		2 游戏时钟 （控制我们循环的帧率）
		3 创建你的 精灵和精灵组（英雄的飞 敌机 背景 子弹
		解耦合
		"""
		print("游戏初始化")
		# 初始化窗口  size  =  width height
		self.screen = pygame.display.set_mode((SCREEN_RECT.width,SCREEN_RECT.height))
		# 游戏时钟
		self.clock = pygame.time.Clock()
		#  创建精灵和精灵组
		self.__create_sprites()

	def start_game(self):
		print("开始游戏")
		while True:
			# 1 刷新帧率
			self.clock.tick(60)
			# 2 监听事件
			self.__handler_event()
			# 3 碰撞检测
			self.__check_collide()
			# 4 更新精灵和精灵组 相当于我们原来说的blit绘制
			self.__update_sprites()
			# 5 刷新屏幕
			pygame.display.update()

	def __create_sprites(self):
		"""创建精灵和精灵组"""
		bg1 = Background('images/background.png')
		bg2 = Background('images/background.png')
		bg2.rect.y = -bg2.rect.height
		self.back_group = pygame.sprite.Group(bg1,bg2)
 


		pass
	# 监听事件
	def __handler_event(self):
		# 你所有的事件 都会被监听到  并且以列表的形式返回
		for event in pygame.event.get():
			# 判断事件类型  pygame.event.QUIT
			if event.type == pygame.QUIT:
				# pygame模块卸载
				pygame.quit()
				# 退出系统
				exit()



	# 碰撞检测
	def __check_collide(self):
		pass
	# 更新精灵和精灵组的方法
	def __update_sprites(self):
		self.back_group.update()
		self.back_group.draw(self.screen)

if __name__ == "__main__":
	# 使用游戏类  创建一个游戏对象
	game = PlaneGame()
	# 开始游戏
	game.start_game() 