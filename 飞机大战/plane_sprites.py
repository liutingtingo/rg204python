import pygame
import random
# 游戏屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 敌机的定时器事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT


class GameSprite(pygame.sprite.Sprite):
	"""游戏精灵基类"""
	def __init__(self,image_name,speed=1):
		# 调用父类的初始化方法
		super().__init__()
		# 加载图像 
		self.image = pygame.image.load(image_name)
		"""
		设置尺寸:
		image 的 get_rect() 方法，
		可以返回 pygame.Rect(0, 0, 图像宽, 图像高) 的对象
		"""
		self.rect = self.image.get_rect()
		# 记录速度
		self.speed = speed

	def update(self,*args):
		# 默认垂直方向移动
		self.rect.y += self.speed 

class Background(GameSprite):
	"""游戏背景精灵类"""
	def __init__(self,is_alt=False):
		image_name = 'images/background.png'
		super().__init__(image_name)
		# 判断是否交替图片 如果是 将图片设置到屏幕顶部
		if is_alt:
			self.rect.y = -self.rect.height

	def update(self):
		# 1 调用父类的方法实现
		super().update()
		# 2 判断是否移出屏幕 如果移除屏幕 将图像设置到屏幕上方
		if self.rect.y >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height


class Enemy(GameSprite):
	"""敌机精灵"""
	def __init__(self):
		# 1 调用父类方法 创建敌机精灵  并且指定敌机图像
		super().__init__('./images/enemy1.png')
		# 2 设置敌机初始速度 随机初始速度1~3
		self.speed = random.randint(1, 3)
		# 3 设置敌机的随机初始位置
		self.rect.bottom = 0
		max_x = SCREEN_RECT.width -self.rect.width
		self.rect.x = random.randint(0, max_x)

	def update(self):
		# 1 调用父类方法 让敌机在垂直方向运动
		super().update()

		# 2 判断是否飞出屏幕 如果是 需要将敌机从精灵组删除
		if self.rect.y>=SCREEN_RECT.height:
			print("敌机飞出屏幕")
			# 将精灵从精灵组中删除
			self.kill()




