from sõnastik import *
valjasta_tervitus()

while True:
    kuva_menu()
    valik = input("\nSisesta valik: ")
    if valik == "1":
        allikas, siht=vali_keelte_suund()
        sona=input(f"Sisesta sõna({allikas}) ")
        tulemus=tolkija(sonad,allikas, siht, sona)
        print(f"Tõlge: {tulemus}")   
    elif valik == "2":
         lisa_sona(sonad)
    elif valik == "3":
        paranda_sona(sonad)     
    elif valik == "4":
        kuva_sonad(sonad)    
    elif valik == "5":
        testi_teadmisi(sonad) 
    elif valik == "6":
        text_to_speech() 
    elif valik == "0":
        break
    else:
        print("Viga! Proovi veel kord.")



