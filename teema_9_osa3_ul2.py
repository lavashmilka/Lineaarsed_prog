import pygame,sys,random
pygame.init()
pink = [255, 153, 255]
red = [255, 0, 0]
# Ekraani suurus
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rallimäng")

# Kell ja font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Taust
background = pygame.image.load("dorogaimpo.png")
background = pygame.transform.scale(background, (640, 480))

# Peamine auto
player_img = pygame.image.load("g.png")
player_img = pygame.transform.scale(player_img, (70, 80))


player_x = 270
player_y = 400
player_speed = 5

pauk_img=pygame.image.load("pauk1.png")
pauk_img=pygame.transform.scale(player_img, (60, 80))
pauk_pos=None

# Координаты полос (X)
lanes = [150, 270, 390]

# Kolm autot
cars_img = [
pygame.transform.scale(pygame.image.load("z.png"), (50, 80)),
pygame.transform.scale(pygame.image.load("a.png"), (50, 80)),
pygame.transform.scale(pygame.image.load("z.png"), (50, 80)),
]

# Каждая  машина — словарь с картинкой и прямоугольником
enemies = []
for i in range(3):
	x = lanes[i]
	y = random.randint(-600, -100)
	img = cars_img[i]
	rect = pygame.Rect(x, y, 50, 80)
	enemies.append({"img": img, "rect": rect})


# Счёт
score = 0
gameover = False


# Игровой цикл
while True:
	screen.blit(background,(0,0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	if not gameover:
		# Управление
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] and player_x > 120:
			player_x -= player_speed
		if keys[pygame.K_RIGHT] and player_x < 470:
			player_x += player_speed

		#Показываем машину ТОЛЬКО если игра НЕ окончена
		
		player_rect = pygame.Rect(player_x, player_y, 50, 80)
		screen.blit(player_img, (player_x, player_y))
		# Двигаем и отображаем каждую машину
		for enemy in enemies:
			enemy["rect"].y += 5
			screen.blit(enemy["img"], enemy["rect"].topleft)
			if enemy["rect"].y > screen_height:
				enemy["rect"].y = random.randint(-600, -100)
				enemy["rect"].x = random.choice(lanes)
				score += 10

			if player_rect.colliderect(enemy["rect"]):
				gameover = True
				pauk_pos=(player_x-5, player_y -10)

			
		# Показываем счёт
			text = font.render("Score: " + str(score), True, (pink))
			screen.blit(text, (20, 20))

	else:
		if pauk_pos:
			screen.blit(pauk_img, pauk_pos)
		over_text = font.render("GAME OVER", True, (pink))
		screen.blit(over_text, (240, 200))
		final_score = font.render("Final Score: " + str(score), True, (red))
		screen.blit(final_score, (240, 240))
	


	pygame.display.flip()
	clock.tick(60)
pygame.quit()
	
