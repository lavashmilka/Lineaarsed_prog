from re import X
import pygame

# def venik():
#     x=20
#     y=5
#     for i in range(20):
#         pygame.draw.line(aken,pruun,(190,120),(x,y),5)
#         x-=10
#         y+=12
#         if i in range(10,20):
#             pygame.draw.line(aken,pruun,(0,0),(x+i,y+i),5)
#         else:
#             pygame.draw.line(aken,pruun,(0,0),(x,y),5)
        



pygame.init()
aken = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Lumemees – Milana") 

valge = (255, 255, 255)
must = (0, 0, 0)
oranž = (255, 165, 0)
sinine = (0, 0, 255)
pruun = (139, 69, 19)
punane=(255,0,0)
aken.fill(must)

pygame.draw.circle(aken, valge, (150, 220), 50) 
pygame.draw.circle(aken, valge, (150, 150), 35) 
pygame.draw.circle(aken, valge, (150, 90), 30) 
pygame.draw.circle(aken, must, (142, 85), 3)
pygame.draw.circle(aken, must, (158, 85), 3)
#smile
pygame.draw.circle(aken,must, (140,105),2)
pygame.draw.circle(aken,must, (145,108),2)
pygame.draw.circle(aken,must, (150,109),2)
pygame.draw.circle(aken,must, (155,108),2)
pygame.draw.circle(aken,must, (160,105),2)
#nuppud
pygame.draw.circle(aken,must, (150,140),3)
pygame.draw.circle(aken,must, (150,150),3)
pygame.draw.circle(aken,must, (150,160),3)
pygame.draw.circle(aken,must, (150,200),5)
pygame.draw.circle(aken,must, (150,220),5)
pygame.draw.circle(aken,must, (150,240),5)
#nina
pygame.draw.polygon(aken, oranž, [(150, 90), (150, 95), (180, 92)])
#müts
pygame.draw.rect(aken, punane, (120, 60, 60, 12))
pygame.draw.rect(aken, sinine, (130, 30, 40, 35))
#käed
pygame.draw.line(aken,pruun,(178,130),(200,100),5)
pygame.draw.line(aken,pruun,(180,160),(220,140),5)
pygame.draw.line(aken, pruun, (190, 200), (190, 120), 5)

pygame.draw.polygon(aken, pruun, [(180, 120), (200, 120), (190, 100)])
# venik()



pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()