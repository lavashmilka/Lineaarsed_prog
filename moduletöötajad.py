from datetime import *
def sisesta_andmed():
    """Kogub töötajate nimed ja sünniaastad, kuni kasutaja lõpetab sisestamise.
    """
    töötajad=[]
    sünniaastad=[]
    while True:
        nimi=input("Sisesta töötaja nimi(bõi vajuta Enter,et lõpetada): ")
        if nimi=="":
            break
        try:
            aasta=int(input("Sisesta sünniaasta: "))
            töötajad.aapend(nimi)
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

def keskmine_vanus(aastad):
    """Arvutab ja kuvab töötajate keskmise vanuse.
    """
    aasta_now=datetime.now().year
    vanused=[aasta_now-a]
    for a in aastad:
        keskmine=sum(vanused)/len(vanused)
        print(f"\nLeskmine vanus: {keskmine:.0f} aastat")

def top_töötajad(nimed,aastad):
    """Kuvab 10 noorimat ja 10 vanimat töötajat.
    """
    aasta_now=datetime.now().year
    vanused=[]
    for i in range(len(nimed)):
        vanused.append((nimed[i], aasta_now-aastad[i]))
        vanused.sort()
        print("\n10 Noorimat töötajat: ")
        for nimi, vanus in vanused[10:]:
            print(f"{nimi}-{vanus}aastat")
        print("\n10 Vanimat töötajat: ")
        for nimi, vanus in vanused[-10:]:
            print(f"{nimi}-{vanus}aastat")

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
        if not leitud:
            print("Sellise aastaga töötajaid ei leitud.")
    except:
        print("Vigane sisestus!")


def kuva_töötajad(nimed, aastad):
    """Kuvab kõik töötajad koos nende sünniaastatega.
    """
    print("\nKõik töötajad ja nende sünniaastad:")
    for i in range(len(nimed)):
        print(f"{nimed[i]} - {aastad[i]}")


def tootajad():
    """Põhifunktsioon, mis pakub kasutajale valiku menüü töötajate andmete analüüsimiseks.
    """
    nimed, aastad = sisesta_andmed()
    if not nimed:
        print("Andmed puuduvad.")
        return



