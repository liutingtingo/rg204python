"""
听着音乐打飞机
这节视频主要讲的是飞机大战的游戏款框架的搭建
我们的目标是 使用面向对象 设计我们飞机大战的游戏类
所以我们需要先来明确我们主程序的职责
在这里我把程序分为两个模块  一个是主程序模块
一个是精灵模块（主要有两个功能 1 工具类   2 设计一些精灵类
包括英雄类  敌机类  背景精灵类  子弹类等等等
"""
# 要使用pygame打飞机 必须先导入pyagme模块
#之前我们学过导入模块有两种方式
#1 在这里我是用第一种 
import pygame
#2
#from pygame import *
from plane_sprites import *

# 我先写在这里
# 初始化
pygame.mixer.init()
# 加载
pygame.mixer.music.load('薛之谦 - 小幸运 (Live).mp3')
# 播放
pygame.mixer.music.play()


class PlaneGame(object):
	"""飞机大战主游戏类"""
	# 初始化方法
	def __init__(self):
		print("游戏初始化")
		"""在开始游戏我们做这么几件事
		1 创建游戏窗口
		2 创建游戏时钟
		3 调用创建精灵和精灵组的方法 （私有方法）
		"""
		# 1 400 700 是因为是事先知道了我背景图片的宽高
		# 在这里我想使用刚刚的常量  但是使用不了 所以我 需要导入模块才能使用
		# 这一块我就不累述了  大家去看笔记  SCREEN_RECT.size会返回一个元组 里面的内容就是宽高
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		# 2 创建游戏时钟 pygame.time.Clcok()为pygame提供的系统方法
		self.clock = pygame.time.Clock()
		# 3 因为创建精灵和精灵组内容比较多 所以我封装成一个方法
		# 接下我们继续 这是调用创建精灵的方法
		self.__create_sprites() # 这一块内容有点问题我们需要调整一下
		# 以上内容应该是属于游戏初始化的时候的设置
		# 4 设置定时器 每隔多少秒 创建 一个敌机
		# pygame.time.set_timer相当于写了一个定时器 每隔1秒钟
		# 去调用一次方法
		# 在这里我想说一下啊pygame这个库已经很久没有维护了
		# 是一个很陈旧的python包  我们只是用它 来更加的让我了解
		#  有一个程序是如何构建的  以及类的设计
		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000) 

		# 我们可以再写一个定时器  发射子弹
		# 比如  我可以每隔0.5秒发射一颗子弹
		pygame.time.set_timer(HERO_FIRE_EVENT,500)
		#  我们在这一步 已经定义了 让系统每隔0.5秒 调用了一下pygame事件
		#  那么我们就需要去我们的事件监听的方法里面去监听事件





	def start_game(self):

		"""在开始游戏这里我们需要做下面几件事"""
		while True:
			# 1 设置帧率
			self.clock.tick(60)
			# 2 事件监听 主要是要监听我们鼠标 键盘的一些事件
			self.__event_handler()
			# 3 碰撞检测 碰撞检测的内容比较  在这里我还没有定义 现在需要补上
			self.__check_collide()
			# 4 更新精灵和精灵组
			self.__update_sprites()
			# 5  更新显示
			pygame.display.update()
			# 在上面  我们调用类方法 并且关于帧率的设置
			# 更新精灵组 碰撞检测 刷新屏幕这些事情 是要实时检测的
			# 所以我写在游戏循环里面
			# 没1/60秒 就会调用一次
			


	# 创建精灵和精灵组
	def __create_sprites(self):
		bg1 = Background()
		# True 就表示是第二张图片
		bg2 = Background(True)
		# 首先你要知道 你需要先 创建背景精灵 需要把精灵的修改一下 
		# bg1 = Background('images/background.png')
		# bg2 = Background('images/background.png')
		# # 我们发现 两张图片的位置我们需要设置一下
		# bg2.rect.y = -bg2.rect.height
		# 我们已经创建了背景精灵  我们接下来可以创建一个背景精灵组
		# 背景组 把我们的背景扔进 背景精灵组
		#------------------------------------------
		# 英雄
		self.hero = Hero()

		self.back_group = pygame.sprite.Group(bg1,bg2)
		# 敌机组
		self.enemy_group = pygame.sprite.Group()
		# 英雄组
		self.hero_group = pygame.sprite.Group(self.hero)



	# 事件监听
	def __event_handler(self):

		# 在这里我先写 事件监听  为啥呢？在调试过程中我好关闭窗口呀
		for event in pygame.event.get():
			# 另外一个方案 返回按键元组  这个我们观察一下就知道了
			# 如果 某个按键按下 对应的值应该会是
			key_pressed = pygame.key.get_pressed()
			if key_pressed[pygame.K_RIGHT]:
				print("向右边移动")
				# 给英雄一个移动速度
				self.hero.speed = 2
			elif key_pressed[pygame.K_LEFT]:
				self.hero.speed =  -2
				print("向左边移动")
			else:
				self.hero.speed = 0

			# pygame.event.get():这是 获取到我们所有的事件
			if event.type == pygame.QUIT:

				# 哈哈 我调用方法 是不是相当于可以关闭我们的窗口啦！！！
				# 在开发的过程中需要  有这种思想 专门的事情由专门的方法去做
				self.__game_over()
				# event.type 相当于说之前 是通过我们按键盘或者
				# 移动鼠标 产生事件  
				# 那么现在呢  是我们自己创造一个事件 每秒执行一次
				#  然后我们去监听我们自己 让 系统去每秒调用的事件
				# 如果调到 那就说明监听成功
				# 那么既然监听监听成功 我需要在监听成功后 
				# 去创建敌机  因为我的目的 就是每秒创建一家敌机
			elif event.type == CREATE_ENEMY_EVENT:
				# 因为我的敌机精灵类还没有写
				# 我这里就先输出一下  
				# 其实这一步  我们完全可以先运行一下
				# 看看有没有出错  看看是不是每秒调用一次
				print("新的敌机产生")
				# 我们添加了敌机  但是但是但是  
				# 没有刷新呀！
				self.enemy_group.add(Enemy())
			elif event.type == HERO_FIRE_EVENT:
				self.hero.fire()
				# 对了  别忘要 去添加子弹
				# 既然是添加子弹   其实  子弹我们也是可以设计成一个类

		# 上面既然我们已经定义了我们每秒钟调一次pygame事件 接下来我们
		#   就需要去监听这个事件

		# 接下来我们就要在我的事件监听里面去 捕获我的事件
			# 这是第一种方式  但是这种方式有一个缺点
			# 就是不能持续移动  这是在监听按下事件 只按下  抬起 才算一次 灵活性不强
			# elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			# 	print("向右移动")
			# elif pygame.key.get_pressed():
			# 	if keys_pressed[pygame.K_RIGHT]:
			# 		print("向右移动")




		
	# 更新精灵和精灵组
	def __update_sprites(self):
		"""更新精灵组"""
		# 我们这一步  先更新背景组
		# 刷新位置
		# self.back_group.update()
		# # 绘制到屏幕上   类似blit
		# self.back_group.draw(self.screen)

		# self.enemy_group.update()
		# self.enemy_group.draw(self.screen)


		# self.hero_group.update()
		# self.enemy_group.draw(self.screen)


		#  到这里我们就可以简写代码了 改造 看了比较清爽 
		for  xxx  in [self.back_group,self.enemy_group,self.hero_group,self.hero.bullets]:
			xxx.update()
			xxx.draw(self.screen)


	def __check_collide(self):
		"""接下来我们就需要完成碰撞检测"""
		# 1 子弹摧毁飞机
		# 子弹炸毁敌机 的情况：
		# 地一个参数和第二个参数是要参与碰撞检测的精灵
		# 地三个参数为 Ture的时候 就是当碰撞的时候 被碰撞的精灵从精灵组移出
		pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
		# 2 敌机撞毁飞机
		enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)

		# 判断列表时候有内容
		if len(enemies)>0:
			# 让英雄牺牲
			self.hero.kill()

			# 结束游戏
			PlaneGame.__game_over()	


	
	def __game_over(self):
		"""游戏结束"""
		print("游戏结束")
		# 这是pygame提供的卸载模块的功能
		pygame.quit()
		# 这是python本身提供的退出脚本的功能
		exit()
		# 总结 ：我们需要先卸载我们的pygame模块  然后退出我们的脚本



# 这个方法就是在我当前方法内生效 在其他模块调不到
if __name__ == "__main__":
	# 创建游戏对象
	game = PlaneGame()
	# 开始游戏
	game.start_game()




"""
来讲讲类的设计吧！   这个游戏类 我们主要就是考虑
逻辑性  当然   你按照之前的学习快速入门的内容 也能搞出
一个打飞机  但是我们需要把我们的代码写的逻辑清晰 并且
分工明确
关于 planeGame类 我们内部是这么设计的
PlaneGame为我们的主游戏类
包含这些属性   screen--->游戏屏幕  clock--->游戏时钟
设计了几个方法 分别做不同的事情
1 初始化方法：设置我们的初始化属性
2 创建精灵 __create_sprites(self):  这里我设置成私有方法
3 start_game(self): 是开始游戏的方法
4 事件监听 event_handler
5 碰撞检测 check_collider
6 更新精灵和精灵组（主要是为了实时去改变和绘制我们精灵
游戏精灵（背景 飞机  敌机  子弹   的位置
7 结束游戏 game_over
大致我们就分析完了  现在来开始写我们的代码
"""
