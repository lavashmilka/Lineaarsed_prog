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
from funktsioonid import *
fail="kontaktid.txt"
kontaktid =kontaktid_failist(fail)

aken=Tk() 
aken.title("Kontaktid")
tk.Label(aken,text="Nimi",bg="lightgreen").pack()
nimi_entry=tk.Entry(aken)
nimi_entry.pack()

nuppude_rida=tk.Frame(aken)
nuppude_rida.pack()


tk.Label(aken,text="Telefon",bg="lightgreen").pack()
telefon_entry=tk.Entry(aken)
telefon_entry.pack(pady=5)


tk.Label(aken,text="Email",bg="lightgreen").pack()
email_entry=tk.Entry(aken)
email_entry.pack()

nuppude_rida=tk.Frame(aken)
nuppude_rida.pack()

tk.Button(nuppude_rida,text="Lisa kontakt", command=lisa_kontakt,bg="lightgreen",font=("Calibri",10)).pack(side="left",pady=5)
tk.Button(nuppude_rida,text="Kuva kontaktid", command=kuva_kontaktid,bg="lightgreen",font=("Calibri",10)).pack(side="left",pady=5)
tk.Button(nuppude_rida,text="Otsi kontakt", command=otsi_kontakt,bg="lightgreen",font=("Calibri",10)).pack(side="left",pady=5)
tk.Button(nuppude_rida,text="Kustuta kontakt", command=kustuta_kontakt,bg="lightgreen",font=("Calibri",10)).pack(side="left",pady=5)
tk.Button(nuppude_rida,text="Paranda kontakt", command=paranda_kontakt,bg="lightgreen",font=("Calibri",10)).pack(side="left",pady=5)
tk.Button(nuppude_rida,text="Sorteeri kontaktid", command=sorteeri_kontakt,bg="lightgreen",font=("Calibri",10)).pack(side="left",pady=5)
tk.Button(nuppude_rida,text="Saada kiri", command=saada_kiri,bg="lightgreen",font=("Calibri",10)).pack(side="left",pady=5)
tk.Button(nuppude_rida,text="Välju", command=salvesta_kontaktid,bg="lightgreen",font=("Calibri",10)).pack(side="left",pady=5)

aken.configure(bg="pink")
aken.iconbitmap("phone.ico")
tekstikast=tk.Text(aken, height=10, width=50)
tekstikast.pack(pady=10)

aken.mainloop()















































# aken.geometry("1200x800")
# aken.configure(bg="pink")  #bg-background(фон)
# aken.resizable(width=False, height=False) #akna suuruse muutmine
# aken.iconbitmap("phone.ico") #akna ikoon
# #aken.attributes("-alpha", 0.9) #прозрачность окна
# pealkiri=Label(aken, text="Tere tulemast!\n See on kontaktid",bg="lightblue", font=("Arial", 20))
# nupp1=Button(aken,text="Lisa kontaktid!",bg="lightgreen",fg="black",font=("Arial",15))
# nupp1.bind("<Button-1>", lisa_kontakt) 
# nupp2=Button(aken,text="Kuva kontaktid!",bg="lightgreen",fg="black",font=("Arial",15))
# nupp2.bind("<Button-1>", kuva_kontaktid) 
# nupp3=Button(aken,text="Otsi kontaktid",bg="lightgreen",fg="black",font=("Arial",15))
# nupp3.bind("<Button-1>", otsi_kontakt) 
# nupp4=Button(aken,text="Kustuta kontaktid!",bg="lightgreen",fg="black",font=("Arial",15))
# nupp4.bind("<Button-1>", kustuta_kontakt) 
# nupp5=Button(aken,text="Paranda kontaktid!",bg="lightgreen",fg="black",font=("Arial",15))
# nupp5.bind("<Button-1>", paranda_kontakt) 
# nupp6=Button(aken,text="Sorteeri kontaktid!",bg="lightgreen",fg="black",font=("Arial",15))
# nupp6.bind("<Button-1>", sorteeri_kontakt) 
# nupp7=Button(aken,text="Sada kiri!",bg="lightgreen",fg="black",font=("Arial",15))
# nupp7.bind("<Button-1>", saada_kiri)
# nupp8=Button(aken,text="Välju!",bg="lightgreen",fg="black",font=("Arial",15))
# nupp8.bind("<Button-1>", salvesta_kontaktid) 



# pilt=PhotoImage(file="iphone.png").subsample(2,2) #subsample-уменьшение изображения в 2 раза)
# pilt_label=Label(aken,image=pilt)






# pealkiri.pack(pady=20)
# nupp1.pack(pady=20)
# nupp2.pack(pady=20)
# nupp3.pack(pady=20)
# nupp4.pack(pady=20)
# nupp5.pack(pady=20)
# nupp6.pack(pady=20)
# nupp7.pack(pady=20)
# nupp8.pack(pady=20)

# # pilt_label.pack(pady=20)
# aken.mainloop()

