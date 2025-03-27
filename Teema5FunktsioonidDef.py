#Ulesanne 1
def arithmetic(arv1:float,arv2:float,tehe:str)-> any:
    """Funktsioon töötab nagu lihtne kalkulaator
    + - liitmine,
    - - lahutamine,
    * - korrutamine
    / - jagamine
    Kui sisend pole järjendis [+,-,/,*],siis tagastab sõne "Tundmatu tehe"
    :param float arv1: Sisend ujukomaarvu tüübina 
    :param float arv2: Sisend ujukomaarvu tüübina
    :param str tehe: Sisesnd listist [+,-,/,*]
    :rtype:varMääremata tüüp (float või str)
    """
    if tehe in ["+","-","/","*"]:
        if arv2==0 and tehe=="/":
            vastus="VIGA"
        else:
            vastus=eval(str(arv1)+tehe+str(arv2))
    else:
        vastus="Tundmatu tehe"
    return vastus
#2
def is_year_leap(aasta:int)->bool:
    """Liigaasta leidmine
    Tagastab True,kui aasta on liigaasta ja False kui aasta on tavaline aasta
    :param int aasta:Sisend kasutajalt
    :rtype: bool tõeväärsuses formaadis tulemus
    """
    if aasta%4==0:
        v=True
    else:
        v=False
    return v
#3
def square(külg:float)->any:
    """Funktsioon leiab
    Ruudu ümbermõõtu
    Ruudu pindala
    Ruudu diagonaal
    :param float S: Sisend ujukomaarv
    :param float P: Sisesnd ujukomaarv
    :param float d: Sisesnd ujukomaarv
    :rtype:tüüp(float)
    """
    S=külg**2
    P=4*külg
    d=(2)**(1/2)
    return S,P,d
#4
def season(param:int)->str:
    """Funktsioon võtab kuu numbri (1-12) ja tagastab sellele vastava aastaaja:
    Talv-(1,2,12)
    Kevad-(3,4,5)
    Suvi-(6,7,8)
    Sügis-(else kuu)
    :param in range(1,13)
    :rtype:tüüp talv,kevad,sügis,suvi
    """
    if param in [1,2,12]:
        H="Talv"
    elif param in [3,4,5]:
        H="Kevad"
    elif param in [6,7,8]:
        H="Suvi"
    else:
        H="Sügis"
    return H
#5
def bank(summa:float,aastad:int)->float:
    """Funktsioon leiab panus
    Igal aastal suureneb tema panuse suurus 10%
    :param aasta: aastate arv, mille jooksul raha hoitakse
    :param summa Esialgne sissemakse(eurodes)
    :rtype:tüüp (int vüi float)
    """
    for aasta in range(aastad):
        summa*=1.1
    return summa

#6
from random import *
def is_prime(a=randint(1,1000))->bool:
    """Funktsioon kontrollib, kas antud arv või algarv
    :param a: Täisarv vahemikus 1 kuni 1000
    rtype:True, kui arv on algarv, vastasel juhul False
    """
    print(a)
    v=True
    for jagaja in range(2,a):
        if a%jagaja==0:
            v=False
    return v
#7
def date(p:int,k:int,a:int)->bool:
    """Funktsioon kontrollib, kas sisestatud kuupäev on kalendris olemas
    :param p: päev(1-31)
    :param k: kuu(1-12)
    :param a: aasta
    :rtype: True, kui kuupäev on kehtiv, vastasel juhul False
    """
    if p in range(1,31) and k in [1,3,5,7,8,10,12] and a>0:
        v=True
    elif p in range(1,30) and k==2 and is_year_leap(a):
        v=True
    elif p in range(1,29) and k==2:
        v=True
    elif p in range(1,31) and k in [4,6,9,11] and a>0:
        v=True
    else:
        v=False
    return v