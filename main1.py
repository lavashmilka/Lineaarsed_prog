from funktsioonid import *
fail="kontaktid.txt"
kontaktid =kontaktid_failist("kontaktid.txt")
while True:
	print("Telefoniraamat menüü\n1. Lisa uus kontakt\n2. Kuva kõik kontaktid\n3. Otsi kontakti\n4. Kustuta kontakt\n5. Muuda kontakti\n6. Sorteeri kontaktid\n7. Saada e-kiri kontaktile\n8. Välju")
	valik = input("Vali tegevus (1-8): ")
	if valik == "1":
		lisa_kontakt(kontaktid)
	elif valik == "2":
		kuva_kontaktid(kontaktid)
	elif valik == "3":
		otsi_kontakt(kontaktid)
	elif valik == "4":
		kustuta_kontakt(kontaktid)
	elif valik == "5":
		paranda_kontakt(kontaktid)
	elif valik == "6":
		sorteeri_kontakt(kontaktid)
	elif valik == "7":
		saada_kiri()
	elif valik == "8":
		salvesta_kontaktid(fail,kontaktid)
		break
	else:
		print("Vale valik, proovi uuesti.")



