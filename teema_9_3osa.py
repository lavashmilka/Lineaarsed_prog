import pygame, sys

pygame.init()

roheline = (0, 255, 0)
pink=[255,153,255]
sinine = (0, 0, 235)
punane = (255, 0, 0)
lGreen = [153, 255, 153]
lBlue=[153,204,255]

#ekraani seaded
screenX = 640
screenY = 480
screen=pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(lBlue)
clock = pygame.time.Clock() #3 Lisame kell
ball = pygame.image.load("pall.png")#graafika laadimine
posX, posY = 580, 400#kiirus ja asukoht
speedX = 1 #2 Lisame samm
gameover = False
while not gameover:
    #fps
    clock. tick(60) #3 paus
    #mängu sulgemine ristist
    events = pygame.event.get()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
            #pildi Lisamine ekraanile
            screen.blit(ball, (posX, posY))
            posX = speedX #2 x koordinaadi muutmine ehk liigub vasakule
            #graafika kuvamine ekraanil
            pygame.display.flip()



pygame.quit()







import pygame, sys 
pygame.init()
red = [255, 0, 0]#värvid
green = [o, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
Green = [153, 255, 153]
Blue = [153, 204, 255]
screenX = 640 #ekraani seaded
screenY = 480
screen=pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine_2")
screen.fill(lBlue)
clock = pygame.time.Clock()
ball = pygame. image.load("pall.png")#graafika laadimine
posX, posY = 0, 0 #kiirus ja asukoht
speed, speedY = 3, 4
gameover = False
while not gameover:
    clock. tick(60)
    #mängu sulgemine ristist
    events = pygame. event.get()
    for i in pygame.event.get(): 
        if i.type == pygame. QUIT:
            sys. exit()
            #pildi Lisamine ekraanile screen. blit(ball, (posX, posY))
            posX += speedx
            posY += speedY
            #kui puudub ääri, siis muudab suunda
            if posX > screenX-ball.get_rect() .width or posX < 0:
                speed = -speedx
            if posY > screenY-ball.get_rect() .height or posY < 0:
                    SpeedY = -speedY
#graafika kuvamine ekraanil
            pygame.display.flip( h
            screen. fill(lBlue)
pygame. quit()
	


import pygame, sys
import random
pygame. init()
red = L255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
Green = [153, 255, 153]
Blue = [153, 204, 255]
screenX = 640
screenY = 480
screen=pygame.display.set_mode([screenX, screenY])
pygame. display.set_caption("Animeerimine")
screen. fill(lBlue)
clock = pygame.time.Clock()
posX, posY = 0, 0 #kiirus ja asukoht
speed, speedY = 3, 3
coords = []#koordinaatide Loomine ja lisamine massiivi
for i in range (10):
    posX = random.randint(1, screenX)
    posY = random.randint(1, screenY)
    coords. append([posX, posY])
gameover = False
while not gameover: clock.tick(120)
events = pygame. event.get(#mängu sulgemine ristist for i in pygame. event.get): if i. type == pygame. QUIT:
sys. exit)
#loendist koordinaadid
for i in range(len(coords)):
pygame. draw.rect(screen, red, [coords[i][0], coords[1][1], 20,20])
coords[i][1] +=1
if
coords [i][1] > screenY:#kui juab alla, siis muudame ruduu alguspunkti # 2
coords [1][1] = random. randint(-40,-10)#
coords [i][0] = random. randint(0, screenX)#
pygame .display.flip()
screen. fill(lBlue)
pygame. quit()
	







