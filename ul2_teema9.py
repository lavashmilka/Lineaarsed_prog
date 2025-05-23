import pygame
import sys
import random

pygame.init()

valge=[255,255,255]
must=[0,0,0]
W, H = 1000, 800
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Ruuduvõrk")


def draw_grid(rows, cols):
	cell_w = W // cols
	cell_h = H // rows
	total = rows * cols
	colors = [(
	random.randint(0, 255),
	random.randint(0, 255),
	random.randint(0, 255)
	) for _ in range(total)]

	index = 0
	for row in range(rows):
		for col in range(cols):
			x, y = col * cell_w, row * cell_h
			pygame.draw.rect(screen, colors[index], (x, y, cell_w, cell_h))
			pygame.draw.rect(screen, (must), (x, y, cell_w, cell_h), 1)
			index += 1


rows = random.randint(10, 30)
cols = random.randint(10, 30)

screen.fill(valge) 
draw_grid(rows, cols)
pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
