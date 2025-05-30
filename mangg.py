import pygame
import random
import sys
import os

pygame.init()

# --- ЭКРАН ---
laius = 800
korgus = 600
ekraan = pygame.display.set_mode((laius, korgus))
pygame.display.set_caption("Hunt püüab mune")
font = pygame.font.SysFont("Arial", 30)

# --- ЦВЕТА ---
valge = (255, 255, 255)
must = (0, 0, 0)

# --- КАРТИНКИ ---
kor_pildid = [pygame.transform.scale(pygame.image.load("kor.png"), (100, 100)),
              pygame.transform.scale(pygame.image.load("kor2.png"), (100, 100))]

taust_pildid = [pygame.transform.scale(pygame.image.load("ferma.png"), (laius, korgus)),
                pygame.transform.scale(pygame.image.load("ferma2.png"), (laius, korgus))]

muna_pildid = [
    pygame.transform.scale(pygame.image.load("muna.png"), (40, 50)),
    pygame.transform.scale(pygame.image.load("muna1.png"), (40, 50)),
    pygame.transform.scale(pygame.image.load("muna2.png"), (40, 50)),
    pygame.transform.scale(pygame.image.load("muna3.png"), (40, 50))
]

broke_pilt = pygame.transform.scale(pygame.image.load("broke1.png"), (40, 50))
coin_pilt = pygame.transform.scale(pygame.image.load("moneta.png"), (30, 30))

# --- СОХРАНЕНИЕ ---
def lae_fail(failinimi, vaikimisi=0):
    try:
        with open(failinimi, "r") as f:
            return int(f.read())
    except:
        return vaikimisi

def salvesta_fail(failinimi, väärtus):
    with open(failinimi, "w") as f:
        f.write(str(väärtus))

# --- ОТРИСОВКА ТЕКСТА ---
def tekst(s, x, y):
    t = font.render(s, True, must)
    ekraan.blit(t, (x, y))

# --- МЕНЮ ---
def menu():
    while True:
        ekraan.fill(valge)
        tekst("Hunt püüab mune", 300, 100)
        tekst("1 - Alusta mängu", 300, 200)
        tekst("2 - Pood", 300, 250)
        tekst("Esc - Välju", 300, 300)
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_1:
                    vali_raskus()
                if e.key == pygame.K_2:
                    pood()
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# --- ВЫБОР СЛОЖНОСТИ ---
def vali_raskus():
    while True:
        ekraan.fill(valge)
        tekst("Vali raskusaste:", 250, 200)
        tekst("1 - Lihtne", 250, 250)
        tekst("2 - Raske", 250, 300)
        tekst("3 - Ekstra raske", 250, 350)
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_1:
                    mäng(1)
                elif e.key == pygame.K_2:
                    mäng(2)
                elif e.key == pygame.K_3:
                    mäng(3)

# --- МАГАЗИН ---
def pood():
    mündid = lae_fail("mündid.txt")
    ostetud_korv = lae_fail("korv.txt")
    ostetud_taust = lae_fail("taust.txt")

    while True:
        ekraan.fill(valge)
        tekst("Pood", 350, 100)
        tekst(f"Sul on {mündid} münti", 300, 150)
        tekst("1 - Osta uus korv (1000 münti)", 200, 250)
        tekst("2 - Osta uus taust (1000 münti)", 200, 300)
        tekst("Esc - Tagasi", 200, 400)
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_1 and mündid >= 1000:
                    mündid -= 1000
                    ostetud_korv = 1
                    salvesta_fail("korv.txt", ostetud_korv)
                    salvesta_fail("mündid.txt", mündid)
                elif e.key == pygame.K_2 and mündid >= 1000:
                    mündid -= 1000
                    ostetud_taust = 1
                    salvesta_fail("taust.txt", ostetud_taust)
                    salvesta_fail("mündid.txt", mündid)
                elif e.key == pygame.K_ESCAPE:
                    return

# --- ИГРА ---
def mäng(raskus):
    kor_x = laius // 2
    kor_y = korgus - 120
    kor_kiirus = 10

    muna_y = 0
    muna_x = random.randint(0, laius - 40)
    muna_pilt = random.choice(muna_pildid)
    on_tuh = False

    punktid = 0
    elud = 3
    highscore = lae_fail("highscore.txt")
    mündid = lae_fail("mündid.txt")

    ostetud_korv = lae_fail("korv.txt")
    ostetud_taust = lae_fail("taust.txt")

    if raskus == 1:
        muna_kiirus = 5
        piirm = 80
    elif raskus == 2:
        muna_kiirus = 8
        piirm = 50
    else:
        muna_kiirus = 12
        piirm = 20

    coin_y = -100
    coin_x = 0
    coin_aktiivne = False
    coin_suurus = 30

    clock = pygame.time.Clock()

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        klahvid = pygame.key.get_pressed()
        if klahvid[pygame.K_LEFT]:
            kor_x -= kor_kiirus
        if klahvid[pygame.K_RIGHT]:
            kor_x += kor_kiirus

        kor_x = max(0, min(kor_x, laius - 100))

        # ДВИЖЕНИЕ ЯЙЦА
        muna_y += muna_kiirus
        if muna_y > korgus:
            if not on_tuh:
                elud -= 1
            muna_y = 0
            muna_x = random.randint(0, laius - 40)
            on_tuh = random.randint(0, 9) == 0
            muna_pilt = broke_pilt if on_tuh else random.choice(muna_pildid)

        # СТОЛКНОВЕНИЕ ЯЙЦА С КОРЗИНОЙ
        if kor_y < muna_y + 50 and kor_y + 100 > muna_y:
            if kor_x < muna_x + 40 and kor_x + 100 > muna_x:
                if on_tuh:
                    elud -= 1
                else:
                    punktid += 1
                muna_y = 0
                muna_x = random.randint(0, laius - 40)
                on_tuh = random.randint(0, 9) == 0
                muna_pilt = broke_pilt if on_tuh else random.choice(muna_pildid)

        # МОНЕТЫ
        if punktid >= piirm and not coin_aktiivne:
            coin_x = random.randint(0, laius - coin_suurus)
            coin_y = 0
            coin_aktiivne = True
            coin_suurus = random.randint(20, 40)

        if coin_aktiivne:
            coin_y += 5
            if kor_y < coin_y + coin_suurus and kor_y + 100 > coin_y:
                if kor_x < coin_x + coin_suurus and kor_x + 100 > coin_x:
                    lisatav = random.randint(100, 200)
                    mündid += lisatav
                    salvesta_fail("mündid.txt", mündid)
                    coin_aktiivne = False
            if coin_y > korgus:
                coin_aktiivne = False

        if elud <= 0:
            if punktid > highscore:
                salvesta_fail("highscore.txt", punktid)
            return

        ekraan.blit(taust_pildid[ostetud_taust], (0, 0))
        ekraan.blit(kor_pildid[ostetud_korv], (kor_x, kor_y))
        ekraan.blit(muna_pilt, (muna_x, muna_y))
        if coin_aktiivne:
            ekraan.blit(pygame.transform.scale(coin_pilt, (coin_suurus, coin_suurus)), (coin_x, coin_y))
        tekst(f"Punktid: {punktid}", 10, 10)
        tekst(f"Elud: {elud}", 10, 50)
        tekst(f"Rekord: {highscore}", 10, 90)
        tekst(f"Mündid: {mündid}", 10, 130)

        pygame.display.update()
        clock.tick(30)

# --- ЗАПУСК ---
menu()





