#Näidised:

#Ainult positiivsed arvud korrutame
a=float(input("A: "))
b=float(input("B: "))
if a>0 and b>0: 
    print(f"Korrutis võrdub: {a*b}")

#Kas a on paaris või paaritu arv?
if a%2==0 and a!=0:
    print(f"Arv {a} on paaris.")
elif a==0:
    print(f"Arv {a} on määramatu.")
else:
    print(f"Arv {a} on paaritu.")

#Ema-robot 5-, 4-, 3-, 2-, 1-
try:
    hinne=int(input("Mis hinne sai täna koolis? "))
    if hinne in range(1,6):
        print("Hinne: ")
        if hinne==5:
            print("Väga hea!")
        elif hinne==4:
            print("Hea!")
        elif hinne==3:
            print("Rahuldav!")
        elif hinne==2 or hinne==1:
            print("Mitte rahuldav")
    else:
        print("Ei ole hinne")
except Exception as e:
    print("Viga: ", e)

nimi="PYTHON"
print(nimi.isupper())
if nimi.isupper():
    print("Suured tähed.")
else:
    print("Ei ole kõik suured tähed.")


#Ülesanne1
nimi=input("Mis on sinu nimi? ")
if nimi=="JUKU":
    print("Lähme kinno!")
    vanus=int(input("Kui vana sa oled? "))
    if vanus<6:
        print("Sulle pilet tasuta!")
    elif vanus<14:
        print("Sulle on vaja osta lastepilet!")
    elif vanus<65:
        print("Sulle on vaja osta täispilet!")
    elif vanus>65:
        print("Sulle on vaja osta sooduspilet!")
    elif vanus<0 and vanus>100:
        print("Viga andmed!")
else:
    print("Ma olen hõivatud!Mine kinno ise")


#Ülesanne 3
try:
    a=float(input("Sisesta toa pikkus: "))
    b=float(input("Sisesta toa laius: "))
    if a>0 and b>0:
        pindala=a*b
        print(f"Põranda pindala on {pindala} ruutmeetri.")
        remont=input("Kas soovid põrandat vahetada?")
        if remont.lower() == "jah" :
            hind=float(input("Sisesta põranda vahetuse hind: "))
            if hind>0:

                koguhind=pindala*hind
                print(f"Põranda vahetamise hind on {koguhind} eurot. ")
            else:
                print("Vale hind!")
        else:
            print("Remondi ei tehta.")
    else:
        print("Viga!")
except:
    print("Viga!")

#Ülesanne 4
try:
    alghind=float(input("Sisesta toode alghind: "))
    if alghind>700:
       soodus=alghind*0.70
       print(f"Soodus hind on {soodus} eurot.")
    else:
        print("Soodustus ei kehti.")
except:
    print("Viga!")

#Ülesanne 5
try:
    temp=float(input("Sisesta temperatuur: "))
    if temp>18:
        print("Temperatuur on üle 18, tuba on soe")
    elif temp==18:
        print("Temperatuur on täpselt 18, see on minimaalne toasoojus.")
    else:
        print("Temperatuur on alla 18, võib olla liiga külm.")
except:
    print("Viga!")

#Ülesanne 6
try:
    pikkus=float(input("Sisesta oma pikkus: "))
    if pikkus<=150:
        print("Oled lühike.")
    elif pikkus<=180:
        print("Oled keskmise pikkusega.")
    else:
        print("Oled pikk.")
except:
    print("Viga!")

#Ülesanne 12
try:
    alghind=float(input("Sisesta toode alghind: "))
    if alghind>10:
        soodus=alghind*0.80
        print(f"Soodustusega hind on {soodus} eurot.")
    else:
        soodus=alghind*0.90
        print(f"Soodustusega hind on {soodus} eurot.")
except:
    print("Viga!")

#Ülesanne 10
try:
    arv1=float(input("Sisesta esimene arv: "))
    arv2=float(input("Sisesta teine arv: "))
    print(f"Esimene arv on {arv1}, teine arv on {arv2}.")
    tehe=input("Mis tehet soovid teha? (+,-,*,/)")
    if tehe=="+":
        tulemus=arv1+arv2
    elif tehe=="-":
        tulemus=arv1-arv2
    elif tehe=="*":
        tulemus=arv1*arv2
    elif tehe=="/":
        if arv2!=0:
            tulemus=arv1/arv2
        else:
           tulemus="viga: nulliga jagamine."
    else:
       tulemus="Viga! Tundmatu tehe!"
    print(f"Tulemus: {tulemus}")
except:
    print("Viga! sisesta ainult arvud.")



