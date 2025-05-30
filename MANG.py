
import pygame
import random
import sys

# Инициализация
pygame.init()

# Экран
ekraan_laius = 800
ekraan_korgus = 600
ekraan = pygame.display.set_mode((ekraan_laius, ekraan_korgus))
pygame.display.set_caption("Hunt püüab mune")

# Цвета
valge = (255, 255, 255)
must = (0, 0, 0)

# Языки
keel= "et"  # Начальный язык
tekst = {
    "et": {
        "title": "Hunt püüab mune",
        "start": "Enter - Alusta mängu",
        "quit": "Esc - Lõpeta",
        "score": "Punktid",
        "lives": "Elud",
        "highscore": "Rekord",
        "gameover": "Mäng läbi! Skoor:",
        "retry": "Enter - Proovi uuesti",
        "difficulty": "Vali raskusaste: 1-Lihtne, 2-Raske, 3-Ekstra raske",
        "lang_switch": "L - Vaheta keelt (eesti/vene)"
    },
    "ru": {
        "title": "Волк ловит яйца",
        "start": "Enter - Начать игру",
        "quit": "Esc - Выход",
        "score": "Очки",
        "lives": "Жизни",
        "highscore": "Рекорд",
        "gameover": "Игра окончена! Счет:",
        "retry": "Enter - Попробуй снова",
        "difficulty": "Выбери уровень: 1-Легкий, 2-Сложный, 3-Экстра сложный",
        "lang_switch": "L - Сменить язык (рус/эст)"
    }
}

# Фон и шрифты
font = pygame.font.SysFont("Arial", 30)

# Загружаем картинки

taust_pilt = [pygame.transform.scale(pygame.image.load('ferma.png'), (ekraan_laius, ekraan_korgus)),
             pygame.transform.scale(pygame.image.load('ferma2.png'), (ekraan_laius, ekraan_korgus))]
kor_pilt =[pygame.transform.scale(pygame.image.load('kor.png'), (100, 100)),
           pygame.transform.scale(pygame.image.load('kor.png'), (100, 100))]


moneta_pilt = pygame.transform.scale(pygame.image.load('moneta.png'), (30, 30))
broke_pilt = pygame.transform.scale(pygame.image.load('broke1.png'), (40, 50))
muna_pildid = [
    pygame.transform.scale(pygame.image.load("muna.png"), (40, 50)),
    pygame.transform.scale(pygame.image.load("muna1.png"), (40, 50)),
    pygame.transform.scale(pygame.image.load("muna2.png"), (40, 50)),
    pygame.transform.scale(pygame.image.load("muna3.png"), (40, 50))
]


def lae_fail(failinimi, vaikimisi=0):
    try:
        with open(failinimi, "r") as f:
            return int(f.read())
    except:
        return vaikimisi

def salvesta_fail(failinimi, väärtus):
    with open(failinimi, "w") as f:
        f.write(str(väärtus))

def tekst_ekraani_uleval(sõnum, x, y):
    t = font.render(sõnum, True, must)
    ekraan.blit(t, (x, y))

def mäng_lõpp(punktid):
    while True:
        ekraan.fill(valge)
        tekst_ekraani_uleval(f"{tekst[keel]['gameover']} {punktid}", 250, 250)
        tekst_ekraani_uleval(tekst[keel]["retry"], 250, 300)
        tekst_ekraani_uleval(tekst[keel]["quit"], 250, 350)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def menüü():
    global keel
    raskus = 1
    while True:
        ekraan.blit(taust_pilt, (0, 0))
        tekst_ekraani_uleval(tekst[keel]["title"], 300, 150)
        tekst_ekraani_uleval(tekst[keel]["start"], 250, 250)
        tekst_ekraani_uleval(tekst[keel]["quit"], 250, 300)
        tekst_ekraani_uleval(tekst[keel]["difficulty"], 150, 400)
        tekst_ekraani_uleval(tekst[keel]["lang_switch"], 150, 450)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mäng(raskus, keel)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_1:
                    raskus = 1
                elif event.key == pygame.K_2:
                    raskus = 2
                elif event.key == pygame.K_3:
                    raskus = 3
                elif event.key == pygame.K_l:
                    keel = "ru" if keel == "et" else "et"

def mäng(raskus, keel):
    if raskus == 1:
        muna_kiirus = 5
        munade_kaevamine_alustab = 80
    elif raskus == 2:
        muna_kiirus = 8
        munade_kaevamine_alustab = 50
    else:
        muna_kiirus = 12
        munade_kaevamine_alustab = 20

    kor_x = ekraan_laius // 2
    kor_y = ekraan_korgus - 120
    kor_kiirus = 10

    muna_x = random.randint(0, ekraan_laius - 40)
    muna_y = 0
    muna_pilt = random.choice(muna_pildid)

    punktid = 0
    elud = 3

    highscore = 0
    try:
        with open("highscore.txt", "r") as f:
            highscore = int(f.read())
    except:
        highscore = 0

    # Монеты: список, где будут позиции и размеры
    moned = []

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        klahvid = pygame.key.get_pressed()
        if klahvid[pygame.K_LEFT]:
            kor_x -= kor_kiirus
        if klahvid[pygame.K_RIGHT]:
            kor_x += kor_kiirus
        if kor_x < 0:
            kor_x = 0
        if kor_x > ekraan_laius - 100:
            kor_x = ekraan_laius - 100

        muna_y += muna_kiirus

        # Монеты появляются, если набрал достаточно очков
        if punktid >= munade_kaevamine_alustab:
            # Добавляем монету рандомно с шансом 2% каждый кадр
            if random.random() < 0.02:
                moned.append({
                    "x": random.randint(0, ekraan_laius - 30),
                    "y": 0,
                    "kiirus": random.randint(3, 6),
                    "suurus": random.randint(15, 30),
                    "väärtus": random.randint(100, 200)
                })

        # Обновляем монеты
        for m in moned:
            ekraan.blit(moneta_pilt, (m["x"], m["y"]))
            # Если монета упала вниз — удаляем
            if m["y"] > ekraan_korgus:
                moned.remove(m)
            # Проверяем ловлит ли монеты корзиной
            elif (kor_y < m["y"] + m["suurus"] and kor_y + 100 > m["y"]) and \
                 (kor_x < m["x"] + m["suurus"] and kor_x + 100 > m["x"]):
                punktid += m["väärtus"]
                moned.remove(m)

        if muna_y > ekraan_korgus:
            elud -= 1
            ekraan.blit(broke_pilt, (muna_x, ekraan_korgus - 50))
            pygame.display.update()
            pygame.time.wait(500)
            muna_y = 0
            muna_x = random.randint(0, ekraan_laius - 40)
            muna_pilt = random.choice(muna_pildid)
            if elud == 0:
                if punktid > highscore:
                    with open("highscore.txt", "w") as f:
                        f.write(str(punktid))
                mäng_lõpp(punktid, keel)

        if kor_y < muna_y + 50 and kor_y + 100 > muna_y:
            if kor_x < muna_x + 40 and kor_x + 100 > muna_x:
                punktid += 1
                muna_y = 0
                muna_x = random.randint(0, ekraan_laius - 40)
                muna_pilt = random.choice(muna_pildid)

        ekraan.blit(taust_pilt, (0, 0))
        ekraan.blit(kor_pilt, (kor_x, kor_y))
        ekraan.blit(muna_pilt, (muna_x, muna_y))
      

        tekst_ekraani_uleval(f"{tekst[keel]['score']}: {punktid}", 10, 10)
        tekst_ekraani_uleval(f"{tekst[keel]['lives']}: {elud}", 10, 50)
        tekst_ekraani_uleval(f"{tekst[keel]['highscore']}: {highscore}", 10, 90)

        pygame.display.update()
        clock.tick(30)

def mäng_lõpp(punktid, keel):
    while True:
        ekraan.blit(taust_pilt, (0, 0))
        tekst_ekraani_uleval(f"{tekst[keel]['gameover']} {punktid}", 250, 250)
        tekst_ekraani_uleval(tekst[keel]["retry"], 250, 300)
        tekst_ekraani_uleval(tekst[keel]["quit"], 250, 350)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menüü(keel)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# Запуск игры
menüü()





