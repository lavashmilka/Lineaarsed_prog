from random import *
s�nad=["V�ilill","Nartsiss","Rukkilill","Lill","Liilia"]
salas�na=choice(s�nad)
k=len(salas�na)
katsed=6
while katsed>0:
    print("_ "*k)
    print(f"On j��nud {katsed} katset")
    katsed-=1
    s�na=input("Sisesta oma variant: ").capitalize()
    if len(s�na)!=k:
        print(f"S�na peab olema {k} t�hte pikk!")
        continue
    if s�na==salas�na:
     print("Hurraa!!")
     break
     tulemus=""
     i=0
     while i<k:
         t�ht=s�na[i]
         if t�ht==salas�na[i]:
             tulemus+=f"[{t�ht}]"
         elif t�ht in salas�na:
             tulemus+=f"({t�ht})"
         else:
             tulemus+=f" {t�ht} "
             i+=1
             print(tulemus)
             katsed-=1
             if katsed==0:
                 print(f"Kahjuks kaotasid! �ige s�na oli: {salas�na}")
