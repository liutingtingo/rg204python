"""
这是我们刚刚说的  另外一个需要设计的模块
在这个模块  放一些常用工具和 基础类  和精灵类
在其他模块调用
"""
import pygame
import random
# 设置游戏屏幕小大 这是一个常量
# 常量见名知意 就是不需要猜测的数字的含义 就是一个固定的数值
# 通过一处修改 其他地方也能生效 统一控制
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

# 我们的父类需要考虑这几个问题
# 1 通用性 2 属性有哪些  方法有哪些   将来谁要用
# 我们自己去定制的精灵类  需要继承 pygame提供的精灵类
"""
我们需要定义的属性有：
image-->图片
rect--->坐标
speed -->速度
"""

# 接下来我们就开始写我们敌机方面的内容 （产生敌机）
# 我先定义一个事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

# 我们还可以定义一个事件常量 （发射子弹）
HERO_FIRE_EVENT = pygame.USEREVENT + 1



class GameSprite(pygame.sprite.Sprite):
	"""游戏精灵的基础类"""
	# 我们其实可以给我们的基础类的速度 设置一个默认值
	def __init__(self,new_image,new_speed=1):
		super().__init__()
		# 我们需要以下3个属性
		# 考虑到通用性  我们需要改造一下代码
		# pygame.image.load pygame提供的方法 主要是加载图片
		self.image = pygame.image.load(new_image)
		# self.image.get_rect() 获取图片的宽高 get_rect() 是pygame提供
		self.rect = self.image.get_rect()
		# 这是将来精灵的移动速度 精灵有：英雄精灵 背景精灵 敌机精灵 子弹精灵
		self.speed = new_speed

	def update(self):
		# 默认垂直方向移动 （这个时候我就要有一个概念 坐标系的y轴控制垂直
		self.rect.y += self.speed


# 那么以上就是我们游戏的基础类 接下来我们需要设置我们的 背景类
# 首先我们需要先明确我们的背景类  继承自我们的游戏精灵类
class Background(GameSprite):
	"""背景精灵类"""
	def __init__(self,is_alt=False):
		"""is_alt 判断是否为另外一张图像
		False表示第一张图像 
		True表示另外一张图像     我们最开始说了  我们是2张图像交替
		在这里我先设置一下 vim快捷键
		"""
		# 因为背景图片是固定的  所以我们可以在背景精灵类直接传图片
		super().__init__('images/background.png')
		if is_alt:
			# 如果是地二张图片 我们让他的初始位置为 -self.rect.height
			self.rect.y = -self.rect.height

	def update(self):
		# 1 调用父类的方法实现 这是实现父类方法
		super().update()
		# 2 判断是否移除屏幕 如果移出屏幕 我们就要将图像设置到屏幕到上方
		# SCREEN_RECT.height 这是我们自己设置的常量  我们可以往上看
		# 其实到这一步 我们就已经把我们的背景类设计完了 接下来我们就去我们的主程序模块调用就行了
		if self.rect.y >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height

# 接下来我们就要设置我们的敌机类
# 我们的敌机类 同样也是继承自我们的精灵基类
class Enemy(GameSprite):
	"""敌机精灵类"""
	def __init__(self):
		# 1 调用父类方法 创建敌机精灵类 并且指定敌机图像
		super().__init__('images/enemy1.png')
		# 2 设置敌机初始速度 稍后设置 （随机数）
		# 我的sublime 没有花事件去调  老是跟我发脾气
		self.speed = random.randint(1, 3)
		# 3 设置敌机的随机初始位置 稍后设置
		# self.rect.y  = self.rect.bottom - self.rect.height
		self.rect.bottom = 0
		# 敌机x轴最大值 需要用屏幕的宽度-敌机自身的宽度
		max_x = SCREEN_RECT.width - self.rect.width
		# 随机一个位置
		self.rect.x = random.randint(0, max_x)


		# 我们发现。。。。。敌机出来的位置在 一条线上
		# 说明  x轴的位置一直没有变 

		def update(self):
			# 1 调用父类方法
			super().update()

			# 2 判断是否飞出屏幕 如果是 需要敌机从精灵组删除
			if self.rect.y >= SCREEN_RECT.height:
				print("敌机飞出屏幕")
				# 移出屏幕  就销毁
				self.kill()
# 接下来我们就设计英雄类和子弹类

# 英雄精灵类
class Hero(GameSprite):
	"""英雄精灵类"""
	def __init__(self):
		# 英雄的初始速度我设置为0
		super().__init__('./images/me1.png',0)

		# 设置初始位置 这是是让我英雄X轴的中心点等于屏幕X轴中心点
		self.rect.centerx = SCREEN_RECT.centerx
		# 这里是设置我飞机的y轴
		self.rect.bottom = SCREEN_RECT.bottom - 120

		# 子弹组
		self.bullets = pygame.sprite.Group()
		# 这样 我们的子弹精灵组 就创建完毕了 我们就要去fire里面修改我们的
		# 方法了

	def update(self):
		# 飞机水平移动
		self.rect.x += self.speed

		# 控制英雄边界 屏幕边界
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right >SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right

	def fire(self):
		# 英雄的方法。。。发射子弹  是一个动作  是一个行为 。。。
		print("发射子弹....")

		for i in (1,2,3):
			# 子弹精灵 我们在 英雄的这个fire（）方法里面去创建
			#1 创建 子弹精灵
			bullet = Bullet()
			#2 设置精灵位置
			bullet.rect.bottom = self.rect.y -20
			bullet.rect.centerx = self.rect.centerx
			#3 将精灵添加到精灵组
			self.bullets.add(bullet)


class Bullet(GameSprite):
	"""子弹精灵"""
	def __init__(self):
		super().__init__('images/bullet1.png',-2)
	def update(self):
		super().update()
		# 判断是否超出屏幕
		if self.rect.bottom < 0:
			self.kill()

"""
正能量
《青年力，让青年的发声更有力》北财见行学院能量朗读文章

幸福都是奋斗出来的，奋斗本身就是一种幸福。只有奋斗的人生才称得上幸福的人生。奋斗是艰辛的，艰难困苦、玉汝于成，没有艰辛就不是真正的奋斗，我们要勇于在艰苦奋斗中净化灵魂、磨砺意志、坚定信念。奋斗是长期的，前人栽树、后人乘凉，伟大事业需要持续奋斗。奋斗是曲折的，“为有牺牲多壮志，敢教日月换新天”，要奋斗就会有牺牲，我们要始终发扬大无畏精神和无私奉献精神。奋斗者是精神最为富足的人，也是最懂得幸福、最享受幸福的人。

新时代是奋斗者的时代。大海不缺一滴水，森林不缺一棵树，单位不缺一个人，但是你的家族，缺少一个扬眉吐气的人，缺少一个让家人过上好日子的人，缺少一个为了梦想而努力持续奋斗的人！人生是很累的，你现在不累，以后就会更累。人生是很苦的，你现在不苦，以后就会更苦。没有靠山，自己就是山！没有天下，自己打天下！没有资本，自己赚资本！活着就该逢山开路，遇水架桥。努力的意义，不要当父母需要你时，除了泪水，一无所有；不要当孩子需要你时，除了惭愧一无所有；不要当自己回首过去，除了蹉跎，一无所有。这就是我们要奋斗的理由。
 
今天“革命尚未成功，我们仍需努力”；我们要实实在在地学，实实在在地干，力戒漂浮。千里之行，始于足下。能动手的不动嘴，能自己干的不要他人干，能巧干的不愚干。天道酬勤，吃得苦中苦，方为人上人，握紧人生方向盘努力奋斗，向幸福出发！
"""