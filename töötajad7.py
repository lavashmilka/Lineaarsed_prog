from moduletöötajad import *
def tootajad():
    """Põhifunktsioon, mis pakub kasutajale valiku menüü töötajate andmete analüüsimiseks."""
    nimed,aastad=sisesta_andmed()
    if not nimed:
        print("Andmed puuduvad.")
        return
    while True:
        print("\nVali tegevus:")
        print("1-Kuva pensionärid\n2-Arvuta keskmine vanus\n3-10 noorimat ja vanimat töötajat\n4-Otsi töötajaid sünniaasta järgi\n5-Kuvada kõik töötajad\n6-Välju")
        valik = input("Valik: ")
        if valik == 1:
                leia_pensionärid(nimed, aastad)
        elif valik == 2:
                keskmine_vanus(aastad)
        elif valik == 3:
                top_töötajad(nimed, aastad)
        elif valik == 4:
                otsi_aasta_järgi(nimed, aastad)
        elif valik == 5:
                kuva_töötajad(nimed, aastad)
        elif valik == 6:
            print("Head aega!")
            break
        else:
            print("Tundmatu valik. Proovi uuesti.")
	

