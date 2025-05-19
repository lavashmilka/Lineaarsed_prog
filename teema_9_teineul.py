import pygame

pygame.init()
aken = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Ülesanne 1.3")

# цвета
valge = (255, 255, 255)
must = (0, 0, 0)
sinine = (100, 100, 255)

# фон
taust = pygame.image.load("pink.png")
taust = pygame.transform.scale(taust, (640, 480))
aken.blit(taust, (0, 0))

# герой
kangelane = pygame.image.load("pers.png")
kangelane = pygame.transform.scale(kangelane, (100, 100))
aken.blit(kangelane, (100, 300))

# рисуем "облако" (bubble)
pygame.draw.polygon(aken, valge, [(220, 270), (500, 270), (500, 200), (400, 180), (300, 200), (220, 200)])

# текст в облаке
font = pygame.font.SysFont("Comic Sans MS", 24)
tekst = font.render("Tere! Mina olen Milana!")
aken.blit(tekst, (230, 210))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
