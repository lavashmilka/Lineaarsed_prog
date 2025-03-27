from Teema5FunktsioonidDef import *
while True:
    try:
        a=float(input("Arv1: "))
        b=float(input("Arv2: "))
        t=input("Tehe: ")
        if t.lowe()=="exit":
              print("Exit programmist")
              break
        vastus=arithmetic(a,b,t)
        print(vastus)
    except:
        print("Viga")

        vastus==arithmetic(float(input("Arv1: ")),float(input("Arv2: ")),input("Tehe: "))
        print(vastus)
#2
aasta=int(input("Mis aasta tahad kontrollida?"))
if aasta>0:
    v=is_year_leap(aasta)
    print(v)
    if v:
        print(f"{aasta} on liigaasta")
    else:
        print(f"{aasta} ei ole liigaasta")

#3
while True:
    try:

        S=float(input("Sisesta ruudu külje pikkus: "))
        if S.lower()=="exit":
            print("Programm lõpetatud.")
            break
        S=float(input("Sisesta ruudu külje pikkus: "))
        P,S,d=square(S)
        print(f"Ümbermõõt: {P}, Pindala: {S}, Diagonaal: {d}")
    except:
        print("Viga, palun uuesti")

#4
while True:
    try:
        param=int(input("Sisesta kuu-(1-12) või 'exit' lõpetamiseks: "))
        if param.lower()=="exit":
            print("Programm lõpetatud.")
            break
        param=int(param)
        print("Aastaaeg: ", season(param))
    except:
        print("Viga, sisesta uuesti.")

#5
while True:
    try:
        summa=input("Sisesta algne sissemakse või 'exit' lõpetamiseks: ")
        if summa.lower()=="exit":
            print("Programm lõpetatud.")
            break
        aastad=input("Sisestaa aastate arv: ")
        if aastad.lower()=="exit":
            print("Programm lõpetatud.")
            break
        summa=float(summa)
        aastad=int(aastad)
        if summa<0 or aastad<0:
            print("Viga")
            continue
        final_amount=deposit(summa,aastad)
        print(f"Pärast {aastad} aastat on teie kontol: {final_amount} eurot")
    except:
        print("Viga")

#6
while True:
    try:
        a=input("Sisesta täisarv: ")
        if a.lower()=="exit":
            print("Viga")
        elif a.lower()=="random":
            print("Jihuslik arv on algarv: ", is_prime)
        else:
            a=int(a)
            if 1<=a<=1000:
                print(f"{a} on algarv: {is_prime(a)}")
            else:
                print("Viga")
    except:
        print("Viga")



#7
while True:
    p=int(input("Sisesta päev: "))
    k=int(input("Sisesta päev: "))
    a=int(input("Sisesta päev: "))
    if date(p,k,a):
        print("Kuupäev eksisteerib")
    else:
        print("Viga")
    v=input("Kas soovid jätkata? (jah/ei): ")
    if v.lower()!="jah":
        break