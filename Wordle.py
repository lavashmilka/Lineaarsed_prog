from random import *
sõnad=["Võilill","Nartsiss","Rukkilill","Lill","Liilia"]
salasõna=choice(sõnad)
k=len(salasõna)
katsed=6
while katsed>0:
    print("_ "*k)
    print(f"On jäänud {katsed} katset")
    katsed-=1
    sõna=input("Sisesta oma variant: ").capitalize()
    if len(sõna)!=k:
        print(f"Sõna peab olema {k} tähte pikk!")
        continue
    if sõna==salasõna:
     print("Hurraa!!")
     break
     tulemus=""
     i=0
     while i<k:
         täht=sõna[i]
         if täht==salasõna[i]:
             tulemus+=f"[{täht}]"
         elif täht in salasõna:
             tulemus+=f"({täht})"
         else:
             tulemus+=f" {täht} "
             i+=1
             print(tulemus)
             katsed-=1
             if katsed==0:
                 print(f"Kahjuks kaotasid! Õige sõna oli: {salasõna}")


