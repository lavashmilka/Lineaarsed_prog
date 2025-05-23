import pygame
import random
import sys

pygame.init()

# Aken
laius, korgus = 800, 600
ekraan = pygame.display.set_mode((laius, korgus))
pygame.display.set_caption("Majake")

# Värvid (teised)
taevas = (180, 220, 255)
lGreen = [153, 255, 153]
red = [255, 0,0]
valge = [255, 255, 255]
muru = (50, 180, 50)
pruun=[139, 69, 19]
maja_varv = (200, 120, 90)
katus_varv = (120, 80, 60)
uks_varv = (80, 40, 30)
aken_valge = (240, 240, 255)
raam = (30, 30, 30)
kollane=[255, 255, 0]
hall = [150, 150, 150]
lilled = [(255, 105, 180), (255, 215, 0), (173, 216, 230)]
korsten_varv = (90, 90, 90)

# Perepilt (teisendatud)
pic = pygame.image.load("doog.png")
pic = pygame.transform.scale(pic, (100, 90))

def joonista_pilved():
    for x in range(300, 800, 200):
        pygame.draw.circle(ekraan, valge, (x, 90), 28)
        pygame.draw.circle(ekraan, valge, (x + 25, 90), 28)
        pygame.draw.circle(ekraan, valge, (x + 12, 70), 28)

def joonista_aknad(x, y, laius):
	suurus = 28
	vasak = x + 15
	parem = x + laius - suurus - 15
	y_aken = y + 35

	for aken_x in [vasak, parem]:
		pygame.draw.rect(ekraan, raam, (aken_x - 2, y_aken - 2, suurus + 4, suurus + 4))
		pygame.draw.rect(ekraan, aken_valge, (aken_x, y_aken, suurus, suurus))
		
def joonista_korsten(house_x, house_y, house_width):
    chimney_width = 20
    chimney_height = 60
    chimney_color = (100, 100, 100)
    # Положение трубы: на правой стороне крыши
    chimney_x = house_x + house_width - 40 # немного левее края дома
    chimney_y = house_y - 60 # труба начинается выше крыши
    pygame.draw.rect(ekraan, chimney_color, (chimney_x, chimney_y, chimney_width, chimney_height))

def joonista_maja():
    house_width = 160
    house_height = 140
    house_x = (laius - house_width) // 2
    house_y = korgus // 2
   
    joonista_korsten(house_x, house_y, house_width)

    pygame.draw.rect(ekraan, pruun, (house_x, house_y, house_width, house_height))
    pygame.draw.polygon(ekraan, hall, [(house_x - 20, house_y),(house_x + house_width + 20, house_y),(house_x + house_width // 2, house_y - 80)])

    door_width = 40
    door_height = 80
    door_x = house_x + (house_width - door_width) // 2
    door_y = house_y + house_height - door_height
    pygame.draw.rect(ekraan, uks_varv, (door_x, door_y, door_width, door_height))
# Рисуем окна после стен и двери
    joonista_aknad(house_x, house_y, house_width)




def paike():
    x = 200
    y = 0
    for i in range(30):
        pygame.draw.line(ekraan, kollane, (0, 0), (x, y), 5)
        x -= 7
        y += 7
        if i in range(10, 20):
            pygame.draw.line(ekraan, kollane, (0, 0), (x + i, y), 5)
        else:
            pygame.draw.line(ekraan, kollane, (0, 0), (x, y), 5)



def joonista_lill(ekraan, x, y):
    pygame.draw.line(ekraan, lGreen, (x, y), (x, y + 60), 4)
    pygame.draw.circle(ekraan, red, (x - 10, y), 10)
    pygame.draw.circle(ekraan, red, (x + 10, y), 10)
    pygame.draw.circle(ekraan, red, (x, y - 10), 10)
    pygame.draw.circle(ekraan, red, (x, y + 10), 10)
    pygame.draw.circle(ekraan, valge, (x, y), 7)

def joonista_aed():
	for x in range(0, laius, 18):
		pygame.draw.rect(ekraan, (160, 82, 45), (x, korgus//2 + 180, 8, 35))



# Taust
ekraan.fill(taevas)
pygame.draw.rect(ekraan, muru, (0,400,800,200))


paike()
joonista_pilved()
joonista_maja()
joonista_aed()
for _ in range(20):
	x=random.randint(20,780)
	y=random.randint(420,580)
joonista_lill(ekraan, 100, 450)
joonista_lill(ekraan, 200, 450)
joonista_lill(ekraan, 350, 450)
joonista_lill(ekraan, 500, 400)
joonista_lill(ekraan, 300, 450)
joonista_lill(ekraan, 250, 450)
joonista_lill(ekraan, 550, 450)
joonista_lill(ekraan, 650, 400)
ekraan.blit(pic, ((laius - 130) // 2, korgus // 2 + 160))

pygame.display.flip()

while True:
	for sündmus in pygame.event.get():
		if sündmus.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	

