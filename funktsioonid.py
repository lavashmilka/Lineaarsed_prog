def kontaktid_failist(fail):
    """Чтение контактов из файла
    """
    kontaktid = []
    try:
        with open(fail, 'r', encoding="utf-8-sig") as f:
            for rida in f:
                nimi, telefon, email = rida.strip().split(",")
                kontaktid.append({'nimi': nimi, 'telefon': telefon, 'email': email})
    except FileNotFoundError:
        pass # Если файла нет, возвращаем пустой список
        return kontaktid

def salvesta_kontaktid(fail, kontaktid):
    """Сохранение контактов в файл
    """
    with open(fail, 'w', encoding="utf-8-sig") as f:
        for k in kontaktid:
            f.write(f"{k['nimi']},{k['telefon']},{k['email']}\n")

def lisa_kontakt(sonad):
    """Добавление нового слова в словарь
    """
    print("Lisame uue kontakti telegoniraamatusse!") #Запрашиваем слово на всех трёх языках, маленькими буквами и убираем лишние пробелы
    uus_nimi = input("Sisesta sõna eesti keeles: ").strip().lower()
    uus_telefon = input("Sisesta sõna vene keeles: ").strip().lower()
    uus_email = input("Sisesta sõna inglise keeles: ").strip().lower()
    sonad.append({'nimi': uus_nimi, 'telefon': uus_telefon, 'email': uus_email}) #Добавляем словарь в список
    print("Uus sõna on lisatud!")

def kuva_kontaktid(sonad):
    """Показывает все слова в словаре
    """
    for m in sonad: 
        print(m)

def otsi_kontakt(kontaktid, nimi):
    """Ищет слово во всех значениях словаря и возвращает его запись
    """
    for m in kontaktid:  #Перебираем все записи в словаре
        if nimi in m.values():  #Если слово найдено в любом из языков
            print(f"Leitud kontakt: {m}")  #Показываем найденное слово и все переводы
            return m  #Возвращаем слово
    return None  #Если слово не найдено

def kustuta_andmed(kontaktid, nimi, email, telefon):
    try:
        kustutav=input("Sisesta kustutav nimi: ")
        kirje=otsi_kontakt(kustutav) 
        if k>0:
            for j in range(k):
                ind=j.index(nimi)
                nimi.pop(ind)
                email.pop(ind)
                telefon.pop(ind)
                print("Andmed on lisatud")
        else:
                print("Andmed puuduvad!")
    except:
            print("Kirjuta ainult tähtede kasutades")


def paranda_sona(kontaktid):
    """Изменение контакта
    """
    parandatav = input("Sisesta muudetava kontakti nimi: ").strip().lower() # Запрашиваем имя контакта
    kirje = None
    for kontakt in kontaktid:
        if kontakt["nimi"].lower() == parandatav:
            kirje = kontakt
            break
            if kirje: # Если контакт найден
                kirje['nimi'] = input("Uus nimi: ").strip().lower()
                kirje['telefon'] = input("Uus telefon: ").strip()
                kirje['email'] = input("Uus e-mail: ").strip().lower()
                print("Kontakt on muudetud!")
            else:
                print("Kontakti ei leitud!") # Если контакт не найден


import smtplib, ssl
from email.message import EmailMessage
def saada_kiri():
    kellele=input("Kellele: ")
    kiri="""<!DOCTYPE html>
<head>
</head>
<body>
<h1>Sending an HTML email from Python</h1>
<p>Hello there,</p>
<a href="https://inspirezone.tech/">Here's a link to an awesome dev
community!</a>
</body>
</html>"""
    smtp_server="smtp.gmail.com"
    smtp_port=587
    kellelt="milamilana2007@gmail.com"
    parool=input("Rakendus parool") #""avhy fgnt ndaw ldwl"
    context=ssl.crate_default_context()
    msg=EmailMessage
    msg.set_content(kiri,subtype="html")
    msg['Subject']="Test"
    msg['From']=kellelt
    msg['To']=kellele
    with open("Pineapple.webp","rb") as f:
        pilt=f.read()
    msg.add_attachment(pilt,maintype="image",subtype="webp",filename="Pineapple.webp")
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