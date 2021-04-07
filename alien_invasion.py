import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	# 初始化屏幕并创建一个屏幕对象
	pygame.init()
	# 用类存储设定参数
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# 创建一艘飞船
	ship = Ship(screen)


	# 开始游戏循环
	while True:

		# 监视键盘鼠标事件
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings, screen, ship)



run_game()