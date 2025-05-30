import pygame
import random
import sys
import os

pygame.init()

#  ЭКРАН 
laius = 800
korgus = 600
ekraan = pygame.display.set_mode((laius, korgus))
pygame.display.set_caption("Hunt püüab mune")
font = pygame.font.SysFont("Verdana", 30,italic=True)

# ЦВЕТА 

must = (0, 0, 0)

#  ЯЗЫК 
tekst = {
    "et": {
        "coins1": "Мündid",
        "title": "Hunt püüab mune",
        "start": "1 - Alusta mängu",
        "shop": "2 - Pood",
        "quit": "Esc - Välju",
        "score": "Punktid",
        "lives": "Elud",
        "highscore": "Rekord",
        "gameover": "Mäng läbi! Skoor:",
        "difficulty": "Vali raskusaste:",
        "easy": "1 - Lihtne",
        "medium": "2 - Raske",
        "hard": "3 - Ekstra raske",
        "retry": "Enter - Proovi uuesti",
        "shop_title": "Pood",
        "coins": "Sul on {m} münti",
        "buy_basket": "1 - Osta uus korv (1000 münti)",
        "buy_bg": "2 - Osta uus taust (1000 münti)",
        "back": "Esc - Tagasi",
        "lang": "L - Vaheta keel"
    },
    "ru": {
        "coins1": "Монеты",
        "title": "Охота за яйцами",
        "start": "1 - Начать игру",
        "shop": "2 - Магазин",
        "quit": "Esc - Выход",
        "score": "Очки",
        "lives": "Жизни",
        "highscore": "Рекорд",
        "gameover": "Игра окончена! Счёт:",
        "difficulty": "Выбери уровень:",
        "easy": "1 - Лёгкий",
        "medium": "2 - Сложный",
        "hard": "3 - Экстра сложный",
        "retry": "Enter - Попробовать снова",
        "shop_title": "Магазин",
        "coins": "У тебя {m} монет",
        "buy_basket": "1 - Купить корзину (1000 монет)",
        "buy_bg": "2 - Купить фон (1000 монет)",
        "back": "Esc - Назад",
        "lang": "L - Сменить язык"
    }
}

keel = ["et"]

#  КАРТИНКИ 
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

broke_pilt = pygame.transform.scale(pygame.image.load("broke.png"), (40, 50))
coin_pilt = pygame.transform.scale(pygame.image.load("moneta.png"), (30, 30))

fon= pygame.transform.scale(pygame.image.load("fon.png"), (laius, korgus))

# СОХРАНЕНИЕ 
def lae_fail(failinimi, vaikimisi=0):
    try:
        with open(failinimi, "r") as f:
            return int(f.read())
    except:
        return vaikimisi

def salvesta_fail(failinimi, väärtus):
    with open(failinimi, "w") as f:
        f.write(str(väärtus))

# ТЕКСТ НА ЭКРАН 
def kirjuta(sõna, x, y):
    t = font.render(sõna, True, must)
    ekraan.blit(t, (x, y))

# МЕНЮ 
def menu():
    while True:
        ekraan.blit(fon,(0,0))
        lang = keel[0]
        kirjuta(tekst[lang]["title"], 300, 100)
        kirjuta(tekst[lang]["start"], 300, 200)
        kirjuta(tekst[lang]["shop"], 300, 250)
        kirjuta(tekst[lang]["quit"], 300, 300)
        kirjuta(tekst[lang]["lang"], 300, 400)
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_1:
                    vali_raskus()
                elif e.key == pygame.K_2:
                    pood()
                elif e.key == pygame.K_l:
                    keel[0] = "ru" if keel[0] == "et" else "et"
                elif e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

#  СЛОЖНОСТЬ 
def vali_raskus():
    while True:
        ekraan.blit(fon,(0,0))
        lang = keel[0]
        kirjuta(tekst[lang]["difficulty"], 250, 200)
        kirjuta(tekst[lang]["easy"], 250, 250)
        kirjuta(tekst[lang]["medium"], 250, 300)
        kirjuta(tekst[lang]["hard"], 250, 350)
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_1:
                    mäng(1)
                    return
                elif e.key == pygame.K_2:
                    mäng(2)
                    return
                elif e.key == pygame.K_3:
                    mäng(3)
                    return

#  МАГАЗИН 
def pood():
    mündid = lae_fail("mündid.txt")
    ostetud_korv = lae_fail("korv.txt")
    ostetud_taust = lae_fail("taust.txt")

    while True:
        ekraan.blit(fon,(0,0))
        lang = keel[0]
        kirjuta(tekst[lang]["shop_title"], 350, 100)
        kirjuta(tekst[lang]["coins"].format(m=mündid), 300, 150)
        kirjuta(tekst[lang]["buy_basket"], 200, 250)
        kirjuta(tekst[lang]["buy_bg"], 200, 300)
        kirjuta(tekst[lang]["back"], 200, 400)
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
                elif e.key == pygame.K_l:
                    keel[0] = "ru" if keel[0] == "et" else "et"

#  ИГРА 
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
            if e.type == pygame.KEYDOWN and e.key == pygame.K_l:
                keel[0] = "ru" if keel[0] == "et" else "et"

        klahvid = pygame.key.get_pressed()
        if klahvid[pygame.K_LEFT]:
            kor_x -= kor_kiirus
        if klahvid[pygame.K_RIGHT]:
            kor_x += kor_kiirus
        kor_x = max(0, min(kor_x, laius - 100))

        muna_y += muna_kiirus
        if muna_y > korgus:
            if not on_tuh:
                elud -= 1
            muna_y = 0
            muna_x = random.randint(0, laius - 40)
            on_tuh = random.randint(0, 9) == 0
            muna_pilt = broke_pilt if on_tuh else random.choice(muna_pildid)

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

        lang = keel[0]
        ekraan.blit(taust_pildid[ostetud_taust], (0, 0))
        ekraan.blit(kor_pildid[ostetud_korv], (kor_x, kor_y))
        ekraan.blit(muna_pilt, (muna_x, muna_y))
        if coin_aktiivne:
            ekraan.blit(pygame.transform.scale(coin_pilt, (coin_suurus, coin_suurus)), (coin_x, coin_y))
        kirjuta(f"{tekst[lang]['score']}: {punktid}", 10, 10)
        kirjuta(f"{tekst[lang]['lives']}: {elud}", 10, 50)
        kirjuta(f"{tekst[lang]['highscore']}: {highscore}", 10, 90)
        kirjuta(f"{tekst[lang]['coins1']}:{mündid}", 10, 130)

        pygame.display.update()
        clock.tick(30)

#  СТАРТ 
menu()

