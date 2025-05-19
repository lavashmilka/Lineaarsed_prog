import pygame
def paike():
    x=200
    y=0
    for i in range(30):
        pygame.draw.line(ekraani_pind,kollane,(0,0),(x,y),5)
        x-=10
        y+=12
        if i in range(10,20):
            pygame.draw.line(ekraani_pind,kollane,(0,0),(x+i,y+i),5)
        else:
            pygame.draw.line(ekraani_pind,kollane,(0,0),(x,y),5)



def pilved():
    pass


def lill():
    pass

pygame.init()
kollane=[255,255,0]
punane=[255,0,0]
hall=[128,128,128]
sinine=[0,0,255]
pruun=[139,69,19]

ekraani_pind=pygame.display.set_mode((800,600))
pygame.display.set_caption("Pygame aken")
ekraani_pind.fill(hall) #заливка
paike()
#polygon - треугольник


pilt=pygame.image.load("nas.jpg")
pilt=pygame.transform.scale(pilt,(100,100))
ekraani_pind.blit(pilt,(300,400))
#tekst
font=pygame.font.SysFont('Arial',50)
sõnum="Tere tulemast!"
teksti_lisamine=font.render(sõnum,True,hall)
ekraani_pind.blit(teksti_lisamine,(500,500))


pygame.display.flip() #отобразить на экране
while True:
    event=pygame.event.poll() #poll- проверяет,что мы нажали
    if event.type==pygame.QUIT: break
pygame.quit()
