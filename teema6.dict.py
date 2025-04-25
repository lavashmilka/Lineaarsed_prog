# Tühja sõnastiku loomine
andmed = {}
# Võtmete ja väärtustega
andmed = {'nimi': 'Mari', 'vanus': 25, 'keel': 'eesti'}
# dict() funktsiooniga
andmed = dict(nimi='Mari', vanus=25, keel='eesti')
print(andmed)
print(andmed["nimi"]) #показать значение ключа "nimi"
print(andmed.get("nimi")) #показать значение ключа "nimi"
print(andmed.get("nimi_","Ei ole sõnastikus")) 
print(andmed.keys()) #показать ключи
print(andmed.values()) #показать значения
for k, v in andmed.items(): #показать список ключ и значение
    print(k, v)
andmed["email"]="ananas@ananas.ee" #добавление ключа и значения
print(andmed)
andmed["prillid"]=True #добавление ключа
print(andmed)
del andmed['prillid'] #удаление ключа
print(andmed)
andmed.update({'nimi':'Kati'}) #Обновление значения имя
print(andmed)

from random import *
read = ['Mis on Python?-programmeerimiskeel', 'Eesti pealinn?-Tallinn', 'Mis on eesti rahvuslill?-Rukkilill', 'Mis on eesti rahvuslind?-Suitsupääsuke']
kus_vas = {}
for rida in read:
    kysimus, vastus = rida.split('-')
    kus_vas[kysimus.strip()] = vastus.strip()
print(kus_vas) # {'Mis on Python?': 'programmeerimiskeel', 'Eesti pealinn?': 'Tallinn', 'Mis on eesti rahvuslill?': 'Rukkilill', 'Mis on eesti rahvuslind?': 'Suitsipääsuke'}
print(kus_vas['Mis on Python?'])

kysimused=list(kus_vas.keys())
while True:
    n=randint(0, len(read)-1)
    valitud_kysimus=kysimused[n]
    print(valitud_kysimus)
    vastus=input("Sisesta vastus: ")
    if kus_vas[valitud_kysimus].lower()==vastus.lower():
        print("Õige vastus")
    elif kus_vas[valitud_kysimus].lower()==0:
        break
    else:
        print("Vale vastus")
      



