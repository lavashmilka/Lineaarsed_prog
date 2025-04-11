from modulepalgad import *

palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

while True:
    print("Andmed")
    print(inimesed)
    print(palgad)
    print("Vajuta:\n1-Andmete lisamiseks\n2-Andmete kustutamiseks nime järgi\n3-Suurima palga leidmiseks\n4-Väiksem palga leidmiseks\n5-Sorteerimine järjend leidmiseks\n6-Võrdsed palgad leidmiseks\n7-Palga otsind leidmiseks\n8-Nimekirjad leidmiseks\n9-Top inimesed leidmiseks\n10-Keskmine palk leidmiseks\n19-Bonus Palk leidmiseks")
    v=int(input())
    if v==1:
        k=int(input("Mitu inimest?: "))
        for i in range(k):
            lisa_andmed(palgad,inimesed)
    elif v==2:
        kustuta_andmed(palgad,inimesed)
    elif v==3:
        suurim_palk(palgad,inimesed)
    elif v==4:
        väiksem_palk(palgad,inimesed)
    elif v==5:
        palgad,inimesed=kas_kah_palk(palgad,inimesed)
    elif v==6:
        võrdsed_palk(palgad,inimesed)
    elif v==7:
        palgaotsing(palgad,inimesed)
    elif v==8:
        nimekirjad(palgad,inimesed)
    elif v==9:
        top(palgad,inimesed)
    elif v==10:
        keskmine(palgad,inimesed)
    elif v==19:
        bonus_salary(palgad,inimesed)
