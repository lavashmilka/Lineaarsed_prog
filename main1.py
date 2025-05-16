# from funktsioonid import *
# fail="kontaktid.txt"
# kontaktid =kontaktid_failist("kontaktid.txt")
# while True:
# 	print("Telefoniraamat menüü\n1. Lisa uus kontakt\n2. Kuva kõik kontaktid\n3. Otsi kontakti\n4. Kustuta kontakt\n5. Muuda kontakti\n6. Sorteeri kontaktid\n7. Saada e-kiri kontaktile\n8. Välju")
# 	valik = input("Vali tegevus (1-8): ")
# 	if valik == "1":
# 		lisa_kontakt(kontaktid)
# 	elif valik == "2":
# 		kuva_kontaktid(kontaktid)
# 	elif valik == "3":
# 		otsi_kontakt(kontaktid)
# 	elif valik == "4":
# 		kustuta_kontakt(kontaktid)
# 	elif valik == "5":
# 		paranda_kontakt(kontaktid)
# 	elif valik == "6":
# 		sorteeri_kontakt(kontaktid)
# 	elif valik == "7":
# 		saada_kiri()
# 	elif valik == "8":
# 		salvesta_kontaktid(fail,kontaktid)
# 		break
# 	else:
# 		print("Vale valik, proovi uuesti.")


import tkinter as tk
from tkinter import *
from tkinter import messagebox
from funk_kontaktid import *
fail="kontaktid.txt"
kontaktid = loe_failist()

def kuva_kontaktid_m():
    tekstikast.delete("1.0", "end")
    for kontakt in kontaktid:
        tekstikast.insert("end", f"{kontakt['nimi']}| {kontakt['telefon']} | {kontakt['email']}\n")

def lisa_kontakt_m():
    nimi = nimi_entry.get()
    telefon = telefon_entry.get()
    email = email_entry.get()
    if nimi and telefon and email:
        lisa_kontakt(kontaktid, nimi,telefon,email)
        salvesta_kontaktid(kontaktid)
        messagebox.showinfo("Edu","kontakt lisatud.")
        nimi_entry.delete(0,'end')
        telefon_entry.delete(0,'end')
        email_entry.delete(0,'end')
        kuva_kontaktid_m()
    else:
        messagebox.showwarning("Teade","Täida kõik väljad")

def otsi_kontakt_m():
    nimi = nimi_entry.get()
    tulemused=otsi_kontakt(kontaktid, nimi)
    if tulemused:
        kontakt=tulemused[0]
        otsingu_viide.set(kontakt["nimi"])
        nimi_entry.delete(0,'end')
        nimi_entry.insert(0, kontakt["nimi"])
        telefon_entry.delete(0,'end')
        telefon_entry.insert(0, kontakt["telefon"])
        email_entry.delete(0,'end')
        email_entry.insert(0, kontakt["email"])
        tekstikast.delete("1.0",'end')
        tekstikast.insert("end", f"Leitud: {kontakt['nimi']} | {kontakt['telefon']} | {kontakt['email']}\n")
    else:
        messagebox.showwarning("Ei leitud", "Kontakt puudub.")


def kustuta_kontakt_m():
    nimi = nimi_entry.get()
    if kustuta_kontakt(kontaktid, nimi):
        salvesta_kontaktid(kontaktid)
        messagebox.showinfo("Kustutatud", f"'{nimi}' kustutati.")
        kuva_kontaktid_m()
    else:
        messagebox.showwarning("Ei leitud", "Kontakt puudub.")

def sorteeri_kontakt_m():
    kontaktid_sorted=sorteeri_kontaktid(kontaktid, "nimi")
    tekstikast.delete("1.0","end")
    for kontakt in kontaktid_sorted:
        tekstikast.insert("end", f"{kontakt['nimi']}, {kontakt['telefon']} , {kontakt['email']}\n")


def muuda_kontakt_m():
    vana_nimi = otsingu_viide.get()
    uus_nimi = nimi_entry.get()
    uus_telefon = telefon_entry.get()
    uus_email = email_entry.get()
    if vana_nimi and uus_email and uus_telefon and uus_email:
        õnnestus=muuda_kontakt(kontaktid, vana_nimi, uus_nimi, uus_telefon, uus_email)
        if õnnestus:
            salvesta_kontaktid(kontaktid)
            messagebox.showinfo("Muudetud", f"'{vana_nimi}' andmed on muudetud.")
            kuva_kontaktid_m()
        else:
            messagebox.showwarning("Ei leitud","Kontakti ei leitud muudatuseks.")
    else:
       messagebox.showwarning("Teade","Puuduvad andmed")


def sorteeri_reverse_m():
    tekstikast.delete("1.0","end")
    k_sorted=sorteeri_reverse(kontaktid,"nimi")
    for kontakt in k_sorted:
        tekstikast.insert("end", f"{kontakt['nimi']} , {kontakt['telefon']} , {kontakt['email']}\n")



def otsi_kontaktnumbri_m():
    telefon = telefon_entry.get()
    tulemused=otsi_kontakt_numbri(kontaktid , telefon)
    if tulemused:
        kontakt=tulemused[0]
        otsingu_viide.set(kontakt["telefon"])
        telefon_entry.delete(0,'end')
        telefon_entry.insert(0, kontakt["telefon"])
        nimi_entry.delete(0,'end')
        nimi_entry.insert(0, kontakt["nimi"])
        email_entry.delete(0,'end')
        email_entry.insert(0, kontakt["email"])
        tekstikast.delete("1.0",'end')
        tekstikast.insert("end", f"Leitud: {kontakt['telefon']}")
    else:
        messagebox.showwarning("Ei leitud", "Kontakt puudub.")


def vali_juhuslik_kontakt_m():
    kontakt=vali_juhuslik_kontakt(kontaktid)
    tekstikast.delete("1.0","end")
    if kontakt:
        tekstikast.insert("end" ,f"Juhuslik kontakt:\n{kontakt['nimi']} | {kontakt['telefon']} | {kontakt['email']}")
    else:
        tekstikast.insert("end","Kontaktide nimekiri on tühi")

def hüüdnimi():
    nimi=nimi_entry.get()
    if nimi:
        hüüdnimi=genereeri_kontakti_hüüdnimi(nimi)
        tekstikast.delete("1.0","end")
        tekstikast.insert("end",f"{nimi} hüüdnimi on {hüüdnimi}")
    else:
        tekstikast.delete("1.0","end")
        tekstikast.insert("end", "Palun sisesta oma nimi")

def kontakti_paevasoovitus_m():
    tulemus=kontakti_paevasoovitus(kontaktid)
    tekstikast.delete("1.0","end")
    tekstikast.insert("end",tulemus)







aken=Tk() 
aken.title("Kontaktid")
otsingu_viide=tk.StringVar() #IntVar() #Muudame StringVar-iks, et saaksime salvestada algse nime
otsingu_viide.set("")
tk.Label(aken,text="Nimi",bg="lightgreen", font=("Calibri",12, "bold italic underline")).pack()
nimi_entry=tk.Entry(aken)
nimi_entry.pack()

tk.Label(aken,text="Telefon",bg="lightgreen", font=("Calibri",12, "bold italic underline")).pack()
telefon_entry=tk.Entry(aken)
telefon_entry.pack(pady=5)

tk.Label(aken,text="Email",bg="lightgreen",font=("Calibri",12, "bold italic underline") ).pack()
email_entry=tk.Entry(aken)
email_entry.pack(pady=5)

rida1=tk.Frame(aken)
rida1.pack(pady=5)

rida2=tk.Frame(aken)
rida2.pack(pady=5)

tk.Button(rida1,text="Lisa kontakt", command=lisa_kontakt_m,font=("Calibri",12, "bold italic"),bg="lightgreen",fg="black").pack(side="left")
tk.Button(rida1,text="Kuva kontaktid", command=kuva_kontaktid_m,font=("Calibri",12, "bold italic"),bg="lightgreen",fg="black").pack(side="left")
tk.Button(rida1,text="Otsi kontakt", command=otsi_kontakt_m,font=("Calibri",12, "bold italic"),bg="lightgreen",fg="black").pack(side="left")
tk.Button(rida1,text="Kustuta kontakt", command=kustuta_kontakt_m,font=("Calibri",12, "bold italic"),bg="lightgreen",fg="black").pack(side="left")
tk.Button(rida1,text="Paranda kontakt", command=muuda_kontakt_m,font=("Calibri",12, "bold italic"),bg="lightgreen",fg="black").pack(side="left")
tk.Button(rida1,text="Sorteeri kontaktid", command= sorteeri_kontakt_m,font=("Calibri",12, "bold italic"),bg="lightgreen",fg="black").pack(side="left")
tk.Button(rida2,text="Sorteeri reverse", command=sorteeri_reverse_m,font=("Calibri",12, "bold italic"),bg="lightgreen",fg="black").pack(side="left")
tk.Button(rida2,text="Otsi telefon", command=otsi_kontaktnumbri_m,font=("Calibri",12, "bold italic"),bg="lightgreen",fg="black").pack(side="left")
tk.Button(rida2,text="Päeva kontakt", command=vali_juhuslik_kontakt_m,font=("Calibri",12, "bold italic"),bg="lightgreen",fg="black").pack(side="left")
tk.Button(rida2,text="Hüüdnimi", command=hüüdnimi,font=("Calibri",12, "bold italic"),bg="lightgreen",fg="black").pack(side="left")
tk.Button(rida2,text="Soovitus", command=kontakti_paevasoovitus_m,font=("Calibri",12, "bold italic"),bg="lightgreen",fg="black").pack(side="left")
aken.configure(bg="pink")
aken.iconbitmap("phone.ico")
tekstikast=tk.Text(aken, height=10, width=50)
tekstikast.pack(pady=10)

aken.mainloop()




















