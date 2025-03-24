from random import *
sınad=["Vıilill","Nartsiss","Rukkilill","Lill","Liilia"]
salasına=choice(sınad)
k=len(salasına)
katsed=6
while katsed>0:
    print("_ "*k)
    print(f"On j‰‰nud {katsed} katset")
    katsed-=1
    sına=input("Sisesta oma variant: ").capitalize()
    if len(sına)!=k:
        print(f"Sına peab olema {k} t‰hte pikk!")
        continue
    if sına==salasına:
     print("Hurraa!!")
     break
     tulemus=""
     i=0
     while i<k:
         t‰ht=sına[i]
         if t‰ht==salasına[i]:
             tulemus+=f"[{t‰ht}]"
         elif t‰ht in salasına:
             tulemus+=f"({t‰ht})"
         else:
             tulemus+=f" {t‰ht} "
             i+=1
             print(tulemus)
             katsed-=1
             if katsed==0:
                 print(f"Kahjuks kaotasid! ’ige sına oli: {salasına}")
