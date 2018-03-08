import pygame
# 初始化方法
pygame.init()

# 初始化游戏窗口
screen = pygame.display.set_mode((480,700))

# 载入游戏背景
bg = pygame.image.load("./images/background.png")

# 确定英雄的初始位置 返回回来的是一个坐标系  (150, 500, 102, 126)
hero_rect = pygame.Rect(200, 500, 102, 126)

# 绘制到屏幕上
screen.blit(bg,(0,0))
# 载入英雄的图片
hero = pygame.image.load("./images/me1.png")
# 绘制到屏幕上
screen.blit(hero,hero_rect)

# 刷新屏幕
pygame.display.update()

# 时钟对象
clock = pygame.time.Clock()

# 英雄飞机的y轴的值
hero_rect = pygame.Rect(200,500, 102, 126)
	

while True:
	# 可以通过 hero_rect.y 获取到当前飞机的y值
	# hero_rect.x hero_rect.height hero_rect.width
	# top bottom left right
	# 每循环一次   y轴的值 -1 500
	hero_rect.y -= 1
	# print(hero_rect.y)
	if hero_rect.y + hero_rect.height <= 0:
	    hero_rect.y = 700
	# if hero_rect.y <= 0:
	# 	hero_rect.y = 700
	screen.blit(bg,(0,0))
	screen.blit(hero,hero_rect)
	pygame.display.update()
	clock.tick(10)

	# 监听事件 pygame.event.get()
	# print(type(pygame.event.get()))
	for event in pygame.event.get():
		print(event)
		if event.type == pygame.KEYDOWN:
			if event.key == 113:
				print("我爱你就像老鼠爱大米")
			elif event.key == 111:
				print("浪漫土耳其")
		
		# if event.type == pygame.KEYDOWN:
		# 	if event.key == 113:
		# 		pygame.quit()
		# 		exit()
			# pygame.quit()
			# exit()
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()




pygame.quit()