import pygame

pygame.init()
aken = pygame.display.set_mode((640, 480))
pygame.display.set_caption("MARIO")
valge = (255, 255, 255)
must = (0, 0, 0)
sinine = (100, 100, 255)


back = pygame.image.load("pink.png")
back = pygame.transform.scale(back, (640, 480))
aken.blit(back, (0, 0))


pers = pygame.image.load("mario.png")
pers = pygame.transform.scale(pers, (100, 100))
aken.blit(pers, (50, 100))

# pygame.draw.rect(aken, valge, (220, 200, 280, 70))
treul= ([(220, 270), (500, 270), (500, 200), (100, 180), (200, 200), (220, 200)])
pygame.draw.polygon(aken,must,treul,width=3)

font = pygame.font.SysFont("Comic Sans MS", 24)
tekst = font.render("Tere! Mina olen Milana!", True, must)
aken.blit(tekst, (230, 210))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
