"""
1、封装游戏中所有需要使用的精灵子类
2、提供游戏的相关工具
"""
import pygame
# 游戏屏幕大小 我设置给一个SCREEN_RECT常量 以便于将来我调用
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

# 基类  父类 背景  英雄  子弹  敌机
# 图片 image  属性   速度   speed 抽父类 
# 刷新界面 update
# 你设计的这个基础类 一定要继承自父类的 精灵类
class PlaneGame(pygame.sprite.Sprite):

	def __init__(self,new_image,new_speed=1):
		super().__init__()
		# 图片
		self.image = pygame.image.load(new_image)
		# 速度
		self.speed = new_speed
		#  位置 获取图片的宽高 get_rect() （0,0，宽,高)
		self.rect = self.image.get_rect()

	def update(self):
		# 默认情况下 垂直方向运动
		self.rect.y += 1
		# self.rect.x += 1

class Background(PlaneGame):
	# def __init__(self,new_image):
	# 	super().__init__(new_image)

	def update(self):
		super().update()
		if self.rect.y == SCREEN_RECT.height:
			self.rect.y = 0

