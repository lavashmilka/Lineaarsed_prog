import funktsioonid
fail="kontaktid.txt"
kontaktid = funktsioonid.loe_kontaktid()
while True:
	print("\nTelefoniraamat menüü\n1. Lisa uus kontakt\n2. Kuva kõik kontaktid\n3. Otsi kontakti\n4. Kustuta kontakt\n5. Muuda kontakti\n6. Sorteeri kontaktid\n7. Saada e-kiri kontaktile\n8. Välju")
	valik = input("Vali tegevus (1-8): ")
	if valik == "1":
		funktsioonid.lisa_kontakt(kontaktid)
	elif valik == "2":
		funktsioonid.kuva_kontaktid(kontaktid)
	elif valik == "3":
		funktsioonid.otsi_kontakt(kontaktid)
	elif valik == "4":
		kontaktid = funktsioonid.kustuta_kontakt(kontaktid)
	elif valik == "5":
		funktsioonid.muuda_kontakt(kontaktid)
	elif valik == "6":
		funktsioonid.sorteeri_kontaktid(kontaktid)
	elif valik == "7":
		funktsioonid.saada_email(kontaktid)
	elif valik == "8":
		print("Head aega!")
		break
	else:
		print("Vale valik, proovi uuesti.")



