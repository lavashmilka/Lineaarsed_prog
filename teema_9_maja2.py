import pygame
import sys
import random
pygame.init()

#ekraani seaded
pind=pygame.display.set_mode([800, 600])
pygame.display.set_caption("Majake")
#värvid
red = [255, 0,0]
green = [0, 255, 0]
blue = [0, 0, 255]
pruun=[139, 69, 19]
pink = [255, 153, 255]
valge = [255, 255, 255]
door_color=[101, 67, 33]
window_frame=[80,80,80]
kollane=[255, 255, 0]
hall = [150, 150, 150]
lGreen = [153, 255, 153]

pic= pygame.image.load("doog.png")
pic= pygame.transform.scale(pic, (100, 50))
pind.fill(blue) # небо
pygame.draw.rect(pind, green, (0, 400, 800, 200)) # трава





def drawHouse(x, y, width, height, screen, door_color):
    house_width = 160
    house_height = 140
    house_x = (width - house_width) // 2
    house_y = height // 2

    pygame.draw.rect(pind, pruun, (house_x, house_y, house_width, house_height)) # стены
    pygame.draw.polygon(pind, pruun, [ # крыша
    (house_x - 20, house_y),
    (house_x + house_width + 20, house_y),
    (house_x + house_width // 2, house_y - 80)
    ])

    drawChimney(house_x, house_y)
    drawDoor(pind, door_color, (door_x, door_y, door_width, door_height))
    drawWindows(house_x, house_y, house_width)


def drawChimney(house_x, house_y):
    chimney_width = 20
    chimney_height = 50
    chimney_x = house_x + 30
    chimney_y = house_y - 80 - chimney_height + 10 # немного ниже пика крыши
    pygame.draw.rect(pind, hall, (chimney_x, chimney_y, chimney_width, chimney_height))


def drawDoor(house_x, house_y, house_width, house_height):
    door_width = 40
    door_height = 70
    door_x = house_x + (house_width - door_width) // 2
    door_y = house_y + house_height - door_height
    pygame.draw.rect(pind, door_color, (door_x, door_y, door_width, door_height))

def drawWindows(house_x, house_y, house_width):
    window_size = 30
    window_y = house_y + 40
    offsets = [20, house_width - 20 - window_size]

    for offset in offsets:
        wx = house_x + offset
        pygame.draw.rect(pind, window_frame, (wx - 2, window_y - 2, window_size + 4, window_size + 4)) # рамка
        pygame.draw.rect(pind, valge, (wx, window_y, window_size, window_size)) # окно
        pygame.draw.line(pind, window_frame, (wx + window_size // 2, window_y), (wx + window_size // 2, window_y + window_size), 2)
        pygame.draw.line(pind, window_frame, (wx, window_y + window_size // 2), (wx + window_size, window_y + window_size // 2), 2)


	


def paike():
    x = 200
    y = 0
    for i in range(30):
        pygame.draw.line(pind, kollane, (0, 0), (x, y), 5)
        x -= 7
        y += 7
        if i in range(10, 20):
            pygame.draw.line(pind, kollane, (0, 0), (x + i, y), 5)
        else:
            pygame.draw.line(pind, kollane, (0, 0), (x, y), 5)

def drawDoor(x, y, width, height, screen, color):
    pass




 



def joonista_lill(ekraan, x, y):
    pygame.draw.line(ekraan, lGreen, (x, y), (x, y + 60), 4)
    pygame.draw.circle(ekraan, red, (x - 10, y), 10)
    pygame.draw.circle(ekraan, red, (x + 10, y), 10)
    pygame.draw.circle(ekraan, red, (x, y - 10), 10)
    pygame.draw.circle(ekraan, red, (x, y + 10), 10)
    pygame.draw.circle(ekraan, valge, (x, y), 7)




	
#kutsun funk välja
drawHouse(600,400,300,400,pind,pruun)  #1-перемещает дом
drawDoor(100, 400, 300, 400, pind, blue)
drawWindows()
drawChimney(100, 400, 300, 400, pind, red)
paike()
joonista_lill(pind, 200, 450)
joonista_lill(pind, 300, 450)
joonista_lill(pind, 350, 450)
joonista_lill(pind, 400, 400)
# joonista_lill(pind, 200, 450)
pygame.display.flip()
while True:
    event=pygame.event.poll() #poll- проверяет,что мы нажали
    if event.type==pygame.QUIT: break
pygame.quit()
