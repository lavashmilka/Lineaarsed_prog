import pygame

pygame.init()
aken = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Lumemees – Аня") # сюда своё имя

valge = (255, 255, 255)
must = (0, 0, 0)
oranž = (255, 165, 0)
sinine = (0, 0, 255)
pruun = (139, 69, 19)
aken.fill(valge)

# keha
pygame.draw.circle(aken,valge, (150, 220), 40) # нижний круг
pygame.draw.circle(aken,valge, (150, 150), 30) # средний круг
pygame.draw.circle(aken,valge, (150, 90), 20) # голова

# глаза
pygame.draw.circle(aken, must, (142, 85), 3)
pygame.draw.circle(aken, must, (158, 85), 3)

# нос
pygame.draw.polygon(aken, oranž, [(150, 90), (150, 95), (180, 92)])

# шляпа
pygame.draw.rect(aken, must, (135, 60, 30, 10))
pygame.draw.rect(aken, must, (140, 40, 20, 20))

# веник
pygame.draw.line(aken, pruun, (190, 200), (190, 120), 5)
pygame.draw.polygon(aken, pruun, [(180, 120), (200, 120), (190, 100)])

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
