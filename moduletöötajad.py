from datetime import *
def sisesta_andmed():
    """Kogub töötajate nimed ja sünniaastad, kuni kasutaja lõpetab sisestamise.
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
    """
    print("\nPensionärid (vanus +65): ")
    aasta_now=datetime.now().year
    for i in range(len(aastad)):
        vanus=aasta_now-aastad[i]
        if vanus>=65:
            print(f"{nimed[i]}-{vanus} aastat")

def keskmine_vanus(nimed,aastad):
    """Arvutab ja kuvab töötajate keskmise vanuse.
    """
    aasta_now=datetime.now().year
    vanused=[]
    summa=0
    for a in aastad:
        vanus = aasta_now - a
        summa+=vanus
        vanused.append(vanus)
    keskmine = sum(vanused) / len(vanused)
    print(f"Keskmine vanus: {keskmine:.0f}")

def top_töötajad(nimed,aastad):    
    """Kuvab 10 noorimat ja 10 vanimat töötajat.
    """
    aasta_now=datetime.now().year
    vanused =[]
    # Считаем возраст каждого и сохраняем в список
    for i in range(len(nimed)):
        vanus = aasta_now - aastad[i]
        vanused.append((nimed[i], vanus)) # кортеж: (имя, возраст)

#  сортировка по возрасту
    for i in range(len(vanused)):
        for j in range(i + 1, len(vanused)):
            if vanused[i][1] > vanused[j][1]: # если текущий старше, меняем местами
                vanused[i], vanused[j] = vanused[j], vanused[i]

# Вывод 10 самых молодых
    print("10 самых молодых работников:")
    for i in range(min(10, len(vanused))):
                        nimi, vanus = vanused[i]
                        print(f"{nimi} - {vanus} лет")

# Вывод 10 самых старых
    print("\n10 самых старых работников:")
    for i in range(min(10, len(vanused))):
                            nimi, vanus = vanused[-(i+1)]
                            print(f"{nimi} - {vanus} лет")



def otsi_aasta_järgi(nimed, aastad):
    """Otsib töötajaid, kes on sündinud määratud aastal.
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
    """
    print("\nKõik töötajad ja nende sünniaastad:")
    for i in range(len(nimed)):
        print(f"{nimed[i]} - {aastad[i]}")










