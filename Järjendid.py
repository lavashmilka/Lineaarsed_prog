sõne="Programmeerimine"
print(sõne)
list_sõne=list(sõne)
print(list_sõne)
print(f"Viies täht: {list_sõne[4]}")
print(f"Sõnes on {len(sõne)} t")
#append
elemendid=[] #список это кв.скобки
for i  in range(5):
    elemendid.append(input(f"{i+1}. element: ")) #добавляет элемент в конце списка-append
print(elemendid)
for e in elemendid:
    print(e)
#extend
list_sõne.extend(elemendid)
print(list_sõne)
print(elemendid)
#insert-ставит значение на определенную позицию
elemendid.insert(0,"A")
print(elemendid)
#remove-удаляет отдельно указанную букву/имеющийся в списке значение
elemendid.remove("A")
print(elemendid)
#pop-тоже удаляет элемент, но если не обозначили,что удалить, то он сам удалит последнйи элемент
elemendid.pop(0)
elemendid.pop()
print(elemendid)
#index-используеться для того чтобы узнать где находиться какойто элемент
ind=list_sõne.index("r")
print(f"Täht r on {ind}-indeksiga")
#count-чтобы узнать сколько вообще всего таких элементов
k=list_sõne.count("r")
print(f"Täht r kohtume {k} korda sõnas {sõne}")
#sort-сортировать, допустим от а до з или 
list_sõne.sort(reverse=True) #наоборот
print(list_sõne)
#reverse-разворачивает список
list_sõne.reverse()
print(list_sõne)
#copy-копия списка
list_sõne2=list_sõne.copy
#clear-очищает список
list_sõne2.clear
print(list_sõne2)

#Ulesanne 1
from string import *
vokaali=["a","o","e","u","i","ü","õ","ö","ä"] #пречесление гласных букв
konsonanti="qwrtpsdfghklzxcvbnmj" #перечесление согласных букв 2 варианта
numbrid=digits
märkid=punctuation
v=k=n=m=t=0
tekst=input("sisend sõna või lause: ").lower() #lower-делает текст или предложение маленькими буквами
tekst_list=list(tekst)
if tekst_list.index(" ")>0:
    print("See on lause")
    for s in tekst_list:
        if s in vokaali:
            v+=1
        elif s in konsonanti:
            k+=1
        elif s in numbrid:
            n+=1
        elif s in märkid:
            m+=1
        elif s==" ":
            t+=1
    print(f"V: {v}\nK: {k}\nN: {n}\nM: {m}\nT: {t}")
else:
    print(f"Kokku on {len(tekst_list)}")

#Ulesanne2
#2.1
nimed=[]
for i in range(5):
    nimi=input("Kirjuta viis nimi: ").lower()
    nimed.append(nimi)
    nimed.sort()
    print("\nNimed tähestikulises järjekorras: ", nimed)
    print("Viimati lisatud nimi:", nimi)
    muutmis_nimi=input("\nSisesta nimi,mida soovid muuta: ")
    if muutmis_nimi in nimed:
        uus_nimi=input("Sisesta uus nimi: ")
        indeks=nimed.index(muutmis_nimi)
        nimed[indeks]=uus_nimi
        print("Uuendatud nimekiri: ", sorted(nimed))
    else:
        print("Sellist nime pole nimekirjas.")
#2.2
õpilased=['Juhan', 'Kati', 'Mario', 'Mati', 'Mati']
unikaalsed_nimed=[]
for nimi in õpilased:
    if nimi not in unikaalsed_nimed:
        unikaalsed_nimed.append(nimi)
print(unikaalsed_nimed)
 
#Ulesanne 7
numbrid=input("Sisesta numbrid(eralda tühiikuga): ")
numbrid=int(nimi) 
for nimi in numbrid:
    suund=input("Kas soovid sorteerida kasvavalt või kahanevalt? (kasv/kahan)").lower()
    if suund=="kasv":
        numbrid.sort(k==abs)
    elif suund=="kahan":
        numbrid.sort(k==abs, reverse=True)
    else:
        print("Vale valik! Kasutame vaikimisi kasvavat soteerimist.")
print("Sorteeritud numbrid:", numbrid)

#Ulesanne 3
sisend=[10,15,30,45,60,25]
for number in sisend:
    print('*' *number)

#Ulesanne 12
   