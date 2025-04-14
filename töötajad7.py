from moduletöötajad import *
nimed, aastad = sisesta_andmed()  # Вводим данные о сотрудниках
if not nimed:
    print("Andmed puuduvad.")
else:
    while True:
        print("\nVali tegevus:")
        print("1-Kuva pensionärid\n2-Arvuta keskmine vanus\n3-10 noorimat ja vanimat töötajat\n4-Otsi töötajaid sünniaasta järgi\n5-Kuvada kõik töötajad\n6-Välju\n7-Bla")  
        try:
            valik = int(input("Valik: "))        
            if valik == 1:
                    leia_pensionärid(nimed, aastad)
            elif valik == 2:
                    keskmine_vanus(nimed,aastad)
            elif valik == 3:
                    top_töötajad(nimed, aastad)
            elif valik == 4:
                    otsi_aasta_järgi(nimed, aastad)
            elif valik == 5:
                    kuva_töötajad(nimed, aastad)
            elif valik == 6:
                    print("Väljumine...")
            elif valik==7:
                bla(nimed,aastad)
                break
            else:
                print("Tundmatu valik. Proovi uuesti.")   
        except:
               print("Sisesta kehtiv number!")        
