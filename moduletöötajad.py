def sisesta_andmed():
    """Kogub töötajate nimed ja sünniaastad, kuni kasutaja lõpetab sisestamise.
    :param list nimed: Список имён работников
    :param list aastad: Список их даты рождения
    """
    töötajad=[]
    sünniaastad=[]
    while True:
        nimi=input("Sisesta töötaja nimi(või vajuta Enter,et lõpetada): ")
        if nimi=="":
            break
        try:
            aasta=int(input("Sisesta sünniaasta: "))
            töötajad.append(nimi)
            sünniaastad.append(aasta)
        except:
            print("Viga!!!")
    return töötajad,sünniaastad

def leia_pensionärid(nimed,aastad):
    """Kuvab kõik töötajad, kelle vanus on 65 või rohkem aastat.
    :param list nimed: Список имён работников
    :param list aastad: Список их даты рождения
    """
    print("\nPensionärid (vanus +65): ")
    aasta_now=2025
    for i in range(len(aastad)):
        vanus=aasta_now-aastad[i]
        if vanus>=65:
            print(f"{nimed[i]}-{vanus} aastat")

def keskmine_vanus(nimed,aastad):
    """Arvutab ja kuvab töötajate keskmise vanuse.
    :param list nimed: Список имён работников
    :param list aastad: Список их даты рождения
    """
    aasta_now = 2025
    vanused = []
    # Считаем возраст каждого и сохраняем в список
    for a in aastad:
        vanus = aasta_now - a
        vanused.append(vanus)
    # Вычисляем средний возраст
    keskmine = sum(vanused) / len(vanused)
    print(f"Keskmine vanus: {round(keskmine)}")

def top_töötajad(nimed, aastad):
    """Находит 10 самых молодых и 10 самых старых работников.
    :param list nimed: Список имён работников
    :param list aastad: Список их даты рождения
    """
    aasta_now = 2025
    vanused = []
    # Считаем возраст каждого и сохраняем в список — сначала возраст, потом имя
    for i in range(len(nimed)):
        vanus = aasta_now - aastad[i]
        vanused.append((vanus, nimed[i])) # (возраст, имя)
    # Сортировка теперь по возрасту, потому что возраст стоит первым
    vanused.sort()
    # Вывод 10 самых молодых работников
    print("10 самых молодых работников:")
    for i in range(min(10, len(vanused))):
        vanus, nimi = vanused[i]
        print(f"{nimi} - {vanus} лет")
    # Инвертируем список, чтобы выводить самых старых работников
    vanused.reverse()
    # Вывод 10 самых старых работников
    print("\n10 самых старых работников:")
    for i in range(min(10, len(vanused))):
        vanus, nimi = vanused[i] # просто берем i-й элемент, потому что список инвертирован
        print(f"{nimi} - {vanus} лет")


def otsi_aasta_järgi(nimed, aastad):
    """Otsib töötajaid, kes on sündinud määratud aastal.
    :param list nimed: Список имён работников
    :param list aastad: Список их даты рождения
    """
    try:
        aasta = int(input("Sisesta sünniaasta, keda otsida: "))
        print(f"\nTöötajad, sündinud aastal {aasta}:")
        leitud = False
        for i in range(len(aastad)):
            if aastad[i] == aasta:
                print(nimed[i])
                leitud = True
        if leitud==False:
            print("Sellise aastaga töötajaid ei leitud.")
    except:
        print("Vigane sisestus!")


def kuva_töötajad(nimed, aastad):
    """Kuvab kõik töötajad koos nende sünniaastatega.
    :param list nimed: Список имён работников
    :param list aastad: Список их даты рождения
    """
    print("\nKõik töötajad ja nende sünniaastad:")
    for i in range(len(nimed)):
        print(f"{nimed[i]} - {aastad[i]}")










