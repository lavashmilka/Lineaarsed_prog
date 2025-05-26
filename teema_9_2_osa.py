import pygame
import sys
import random
pygame.init() #Pygam
#värvid
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]
ekraani_pind = pygame.display.set_mode( (640, 480) )
ekraani_pind. fill( lGreen )
pygame.display.set_caption("Esimene mäng")
gameover = False
while not gameover:
#Lisame pildid
    youWin = pygame. image. load("win.jpg")
    youWin = pygame. transform.scale(youWin, [300, 200])
    ekraani_pind.blit(youWin, [180, 100])
    pygame. display.flip()
#mängu sulgemine ristist for i in pygame.event.get(): if i. type == pygame. QUIT:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            sys.exit()
pygame.quit()




# import pygame
# import random
# import sys
# pygame. init()
# #värvid
# r=random. randint(0, 255)
# g=random.randint(0, 255)
# b=random. randint(0, 255)
# varv = [r, g,b]
# lGreen = [153, 255, 153]

# pind=pygame.display. set_mode([640, 480])
# pygame.display.set_caption("Juhuslikud kujundid")
# pind.fill(lGreen)
# for i in range (1,10):
#     x = random.randint(0, 620)
#     y = random. randint(0, 460)
#     pygame.draw.rect(pind, varv, [x, y, 20, 20])
#     pygame.display. flip()
# while True:
#     event = pygame.event.poll()
#     if event. type == pygame. QUIT:
#         break
# pygame.quit()




# import pygame
# import sys
# import random
# pygame.init()


# #värvid
# red = [255, 0,0]
# green = [0, 255, 0]
# blue = [0, 0, 255]
# pink = [255, 153, 255]
# lGreen = [153, 255, 153]


# #ekraani seaded
# pind=pygame.display.set_mode([640, 480])
# pygame.display.set_caption("Majake")
# pind.fill(lGreen)


# #Funktsioonid
# def drawHouse(x, y, width, height, screen, color):
#     points = [(x, y- ((3/4.0) * height)), (x,y), (x+width, y), (x+width, y-(3/4.0) * height),
#         (x, y- ((3/4.0) * height)), (x + width/2.0,y-height), (x+width, y-(3/4.0)*height)]
#     lineThickness = 3
#     pygame.draw.lines(screen, color, False, points, lineThickness)
	
# #kutsun funk välja
# drawHouse(100,400,300,400,pind,red)
# pygame.display.flip()
# while True:
#     event=pygame.event.poll() #poll- проверяет,что мы нажали
#     if event.type==pygame.QUIT: break
# pygame.quit()