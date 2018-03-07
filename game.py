#from pygame import pygame
import pygame

# 初始化方法
pygame.init()

# 创建游戏屏幕宽和高 
screen = pygame.display.set_mode((480,700))
# 游戏循环
# while True:
# 	pass
# 加载图片
bg = pygame.image.load("./images/background.png")
# 绘制到屏幕上
screen.blit(bg,(0,0))
# 刷新屏幕



# 创建英雄
hero = pygame.image.load("./images/me1.png")
# 绘制到屏幕上
screen.blit(hero,(200,500))
# 刷新屏幕
pygame.display.update()


while True:
	pass

# 退出(卸载)
pygame.quit()