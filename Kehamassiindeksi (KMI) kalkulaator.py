print("Tere! Olen sinu uus sıber - Python!")
nimi = input("Palun sisesta oma nimi: ")
print(f"{nimi}, oi kui ilus nimi!")
vastus = input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")

if vastus == "1":  
    try:
        pikkus = int(input("Palun sisesta oma pikkus sentimeetrites: "))  
        mass = float(input("Palun sisesta oma kehakaal kilogrammides: "))  

        pikkus_m = pikkus / 100  
        kmi = mass / (pikkus_m ** 2)  
        print(f"{nimi}! Sinu keha indeks on: {kmi:.1f}")
        
        if kmi < 16:
            print("Tervisele ohtlik alakaal")
        elif 16 <= kmi < 19:
            print("Alakaal")
        elif 19 <= kmi < 20:
            print("Normaalkaal")
        elif 20 <= kmi < 25:
            print("Normaalkaal")
        elif 25 <= kmi < 26:
            print("‹lekaal")
        elif 26 <= kmi < 30:
            print("Rasvumine")
        elif 30 <= kmi < 31:
            print("Tugev rasvumine")
        elif 31 <= kmi < 35:
            print("Tervisele ohtlik rasvumine")
        elif kmi >= 35:
            print("Tervisele ohtlik rasvumine")
    except ValueError:
        print("Vigane sisend! Palun sisesta kehtivad numbrilised v‰‰rtused.")
    
elif vastus == "0":  
    print("Kahju! See on v‰ga kasulik info!")

else:
    print("Vigane valik! Palun sisesta 0 vıi 1.")

print(f"Kohtumiseni, {nimi}! Igavesti Sinu, Python!")
