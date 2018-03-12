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
		pass	
	# 事件监听
	def __event_handler(self):
		# 在这里我先写 事件监听  为啥呢？在调试过程中我好关闭窗口呀
		for event in pygame.event.get():
			# pygame.event.get():这是 获取到我们所有的事件
			if event.type == pygame.QUIT:
				# 哈哈 我调用方法 是不是相当于可以关闭我们的窗口啦！！！
				# 在开发的过程中需要  有这种思想 专门的事情由专门的方法去做
				self.__game_over()
		
	# 更新精灵和精灵组
	def __update_sprites(self):
		pass
	def __check_collide(self):
		pass

	
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
