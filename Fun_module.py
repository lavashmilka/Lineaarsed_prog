from Teema5FunktsioonidDef import *

a=float(input("Arv1: "))
b=float(input("Arv2: "))
t=input("Tehe: ")
vastus=arithmetic(a,b,t)
print(vastus)

vastus==arithmetic(float(input("Arv1: ")),float(input("Arv2: ")),input("Tehe: "))
print(vastus)

aasta=int(input("Mis aasta tahad kontrollida?"))
if aasta>0:
    v=is_year_leap(aasta)
    print(v)
    if v:
        print(f"{aasta} on liigaasta")
    else:
        print(f"{aasta} ei ole liigaasta")