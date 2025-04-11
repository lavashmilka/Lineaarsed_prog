p=[]
i=[]
def lisa_andmed(p:list,i:list):
    """Funktsioon leiab nende palgad ja mitu inimesed
    :param i: Sisend tähed
    :param p: Sisend numbrid
    :rtype:Määremata tüüp (str või float)
    """
    while True:
        try:
            nimi=input("Nimi: ")
            if nimi.isalpha():
                try:
                    palk=float(input("Palk: "))
                except:
                    print("Palk on arv")
                break
                print("Andmed on lisatud")
            else:
                print("Kirjuta ainult tähed")
        except:
            print("Kirjuta ainult tähtede kasutades")
    p.append(palk)
    i.append(nimi)

def kustuta_andmed(p:list,i:list):
    """Funktsioon kustuta palgad ja inimesed,kui i ja p>0
    :param i: Sisend tähed
    :param p: Sisend numbrid
    :param nimi: Sisend str
    :rtype:Määremata tüüp (str või float)
    """
    try:
            nimi=input("Nimi: ")
            if nimi.isalpha():
                k=i.count(nimi)
                if k>0:
                    for j in range(k):
                        ind=i.index(nimi)
                        i.pop(ind)
                        p.pop(ind)
                        print("Andmed on lisatud")
            else:
                print("Andmed puuduvad!")
    except:
            print("Kirjuta ainult tähtede kasutades")

def suurim_palk(p:list,i:list):
    """Funktsioon leiab suurim palgad inimestel
    :param i: Sisend tähed
    :param p: Sisend numbrid
    :rtype:Määremata tüüp (str või float)
    """
    suurim=max(p)
    print(f"Suurim palk on {suurim}")
    k=p.count(suurim)
    ind=p.index(suurim)
    for j in range(k):
        ind=p.index(suurim,ind)
        print(f"Saab kätte {i[ind]}")
        ind+=1

def väiksem_palk(p:list,i:list):
    """Funktsioon leiab väiksem palgad inimestel
    :param i: Sisend tähed
    :param p: Sisend numbrid
    :rtype:Määremata tüüp (str või float)
    """
    väiksem=min(p)
    print(f"Väiksem palk on {väiksem}")
    k=p.count(väiksem)
    ind=p.index(väiksem)
    for j in range(k):
        ind=p.index(väiksem,ind)
        print(f"Saab kätte {i[ind]}")
        ind+=1

def kas_kah_palk(p:list,i:list)->any:
    """Funktsioon järjesab palgad kasvavas ja kahanevas järjekorras koos nimedega
    :param inimesed: Inimeste nimekiri
    :param palgad: Palkade nimekiri
    :rtype: any
    """
    while True:
        try:
            v=input("Vali märk: >(kasvav) või < (kahanev)")
            if v in('>','<'):
                break
            else:
                print("Ainult "<" ja ">"")
        except:
            print("Viga! Proovi uuesti!")
            for n in range(0,len(i)):
                for m in range(n,len(i)):
                    if eval(str(p[n])+v+str+(p[m])):
                        p[n],p[m]=p[m],p[n]
                        i[n],i[m]=i[m],i[n]

       

def võrdsed_palk(p:list,i:list):
    """Funktsioon leiab kes saavad võrdset palka, ja kui palju neid on ja kuvada nende andmed ekraanile
    :param inimesed: Inimeste nimekiri
    :param palgad: Palkade nimekiri
    :rtype:none
    """
    hulk=set(p)
    print(hulk)
    for palk in hulk:
        k=p.count(palk)
        if k>1:
            print(f"Palk {palk}")
            ind=p.index(palk)
            for j in range(k):
                ind=p.index(palk,ind)
                print(f"Saab kätte {i[ind]}")
                ind+=1


def palgaotsing(p:list,i:list):
    """Funktsioon Teha palgaotsing isiku nime järgi.
    :param i: Inimeste nimekiri
    :param p: Palkade nimekiri
    :rtype:none
    """
    nimi=input("Sisesta nimi mida sa sooviks: ")
    leitud=False
    for j in range(len(i)):
        if i[j]==nimi:
            print(f"{nimi} palk: {p[j]}")
            leitud=True
    if leitud==False:
        print(f"{nimi} kohta andmeid ei leitud.")



             
def nimekirjad(p:list,i:list):
    """Väljundab nimekirja inimestest (koos palgaga), kes saavad rohkem/vähem kui määratud summa.
    :param p: Inimeste nimekiri
    :param i: Palkade nimekiri
    :rtype:float
    """          
    try:
        summa = float(input("Sisesta summa: "))
        valik = input("Kas soovid rohkem või vähem? (r/v): ").lower()
        if valik == "r":
                for h in range(len(p)):
                    if p[h] > summa:
                        print(i[h], "-", p[h])
        elif valik == "v":
            for h in range(len(p)):
                if p[h] < summa:
                    print(i[h], "-", p[h])
        else:
              print("Vale valik!")
    except:
          print("Vigane sisend!")
	
      
def top(p:list,i:list):
    """T vaeseimad ja rikkamad inimesed
    :param p: Inimeste nimekiri
    :param i: Palkade nimekiri
    :rtype:none
    """
    suurimad_palgad = max(p)
    print(f"Suurim palk: {suurim_palk} ")
    for j in range(len(p)):
        if p[j]==suurim_palk:
            print(f"{i[j]}")
    väiksem_palk = min(p)
    print(f"Väiksem palk: {väiksem_palk} ")
    for j in range(len(p)):
        if p[j]==väiksem_palk:
            print(f"{i[j]}")
   
def keskmine(p:list,i:list):
    """Keskmine palk ja selle saaja nimi/nimed
    :param p: Inimeste nimekiri
    :param i: Palkade nimekiri
    :rtype:none
    """
    a=sum(p)/len(p)
    print(f"Keskmine palk: {a:.0f}")
    print("Keskmine palgaga inimesed: ")
    for m in range(len(p)):
        if p[m]==a:
            print(i[m],"-",p[m])
        else:
            print("Viga")
       

def bonus_salary(p: list, i:list):
    """Oma funktsioon annab palgatud töötajale täiendava palgaõusu, võimaldades valida palgaõusu protsendi
    :param i: Inimeste nimekiri
    :param p: Palkade nimekiri
    :rtype: None
    """
    for idx, (name,salary) in enumerate(zip(i,p),1):
        print("\nCurrent employees and salaries: ")
        print(f"{idx}. {name}: {salary}$")
    try:
        choice=int(input("Valige töötaja: ")) -1
        bonus=float(input("Kirjutage mittu protsentis palk tõuseb: "))
        if 0 <= choice < len(i) and bonus > 0:
            original_salary=p[choice]
            bonus_to = bonus / 100
            bonus_salary = original_salary * bonus_to + original_salary
            print(f"New salary is: {bonus_salary}$")
        else:
            print("Valige eksisteeriv töötaja ja valige bonus rohkem kui 0")
    except:
        print("Error!")











###DRACULA THEME
        
