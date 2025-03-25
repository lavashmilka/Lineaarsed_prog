from random import *
sõnad=["Võilill","Nartsiss","Rukkilill","Lill","Liilia"]
salasõna=choice(sõnad)
salasõnalist=list(salasõna)
k=len(salasõna)
katsed=6
while katsed>0:
    print("_ "*k)
    print(f"On jäänud {katsed} katset")
    katsed-=1
    sõna=input("Sisesta oma variant: ").capitalize()
    sõnalist=list(sõna)
    for a in range (0,k,1):
        o+=1
        if sõnalist[0]==salasõnalist[0]:
            print(sõnalist[0],end=" ")
        else:
            print("*",end=" ")
    print()
    if sõna==salasõna:
        print("Huraa!")
        break
    else:
        print("Vale sõna!" ,6-p-1, "on jäänud katset.")
        p-=1
        sõnalist=sõnalist.append(sõna)
        print(sõnalist)
