import smtplib,ssl
from email.message import EmailMessage

def kontaktid_failist(fail:str):
    kontaktid=[]
    with open(fail,'r',encoding="utf-8-sig") as f:
        for rida in f:
            nimi,email,telefon=rida.strip().split(",")
            kontaktid.append({'nimi':nimi,'email':email,'telefon':telefon})
    return kontaktid

def salvesta_kontaktid(fail:str,järjend:list):
    with open(fail,'w',encoding="utf-8-sig") as f:
        for k in järjend:
            f.write(f"{k['nimi']},{k['email']},{k['telefon']}\n")

def lisa_kontakt(kontaktid):
    """Добавление нового контакта в телефонную книгу
    """
    print("Lisame uue kontakti!") 
    uus_nimi = input("Sisesta nimi: ").strip().lower()
    uus_email = input("Sisesta email: ").strip().lower()
    uus_telefon = input("Sisesta telefon: ").strip()
    kontaktid.append({'nimi': uus_nimi, 'email': uus_email, 'telefon': uus_telefon}) 
    print("Uus kontakt on lisatud!")

def kuva_kontaktid(kontaktid):
    """Показывает все данные в телефонной книге
    """
    for k in kontaktid:
            print(k)

def otsi_kontakt(kontaktid):
    """Ищет данные в телефонной книге
    """
    nimi=input("Sisesta nimi: ").strip().lower()
    for kontakt in kontaktid:  
        if nimi in kontakt['nimi'].lower():  
            print(f"Leitud: {kontakt}") 
            return kontakt  
    return None   

def kustuta_kontakt(kontaktid):
    """Удаление контакта 
    """
    kontakt=otsi_kontakt(kontaktid)
    if kontakt in kontaktid:
        kontaktid.remove(kontakt)  
        print("Kontakt kustutatud!")

def paranda_kontakt(kontaktid):
    """Изменение контакта
    """
    andmed=otsi_kontakt(kontaktid)  
    if andmed:  
        andmed['nimi']=input("Uus nimi: ")  
        andmed['telefon']=input("Uus telefon: ")  
        andmed['email']=input("Uus email: ")  
        print("Parandatud!") 
    else:
        print("Sõna ei leitud!")  

def sorteeri_kontakt(kontaktid):
    """Сортировка контактов по имени, телефону или email
    """
    s = input("Sorteeri mille järgi (nimi, telefon, email): ").strip().lower()
    if s not in ["nimi", "telefon", "email"]:
        print("Vale valik.")
        return
    ajutine = []
    for kontakt in kontaktid:
        ajutine.append([kontakt[s].lower(), kontakt])
    ajutine.sort()
    for i in range(len(kontaktid)):
        kontaktid[i] = ajutine[i][1]
    print("Sorteeritud.")


def saada_kiri():
    kellele=input("Kellele: ")
    smtp_server="smtp.gmail.com"
    smtp_port=587
    kellelt="milamilana2007@gmail.com"
    parool=input("Rakendus parool: ") #""avhy fgnt ndaw ldwl"
    context=ssl.crate_default_context()
    msg=EmailMessage
    msg['Subject']="Test"
    msg['From']=kellelt
    msg['To']=kellele
    msg.set_content("Tere, see on test e-kiri")
    try:
        server=smtplib.SMTP(smtp_server, smtp_port)
        server.starttls(context=context)
        server.login(kellelt,parool)
        server.send_message(msg)
        print("Kiri saadetud")
    except Exception as e:
        print("Viga: ",e)
    finally:
        server.quit()