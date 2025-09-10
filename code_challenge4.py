print("		Welcome to Manga Read Recomendations")

a = input("Input Genre (Action/Horror/Romance) --> ").lower()

if a == "action":
	b = input("How long Manga should be? (Short/Medium/Long) --> ")
	if b.lower() == "short":
		c = input("Decade/s With short Action books (2000s, 2010s) --> ")

		if c == "2000":
			print("Manga Books in 2000s \n Death Note : (2004) \n Gin Tama : (2004)")

		elif c == "2010":
			print("Manga Books in 2010s \n My Hero Academia : (2010) \n Attack on Titan : (2010)")

	elif b.lower() == "medium":
		c = input("Decade/s available With medium Action books (1990s, 2020s) --> ")

		if c == "1990":
			print("Manga Books in 1990s \n Slam Dunk : (1993) \n AKIRA : (1995)")

		elif c == "2020":
			print("Manga Books in 2020s \n Spy x Family : (2020) \n Demon Slayer : (2020)")

	elif b.lower() == "long":
		c = input("Decade/s available with Long Action books (1980s, 1970s) --> ")

		if c == "1980":
			print("Manga Books in 1980s \n Fist of the North Star  : (1983) \n Dragon Ball : (1984)")
		elif c == "1970":
			print("Manga Books in 1970s \n  Golgo 13 : (1970) \n Lupin the 3rd by Monkey Punch : (1970)")

elif a == "horror":
	b = input("How long Manga should be? (Short/Medium/Long) --> ")
	if b.lower() == "short":
		c = input("Decade/s With short Horror books (2000s, 2010s) --> ")

		if c == "2000":
			print("Manga Books in 2000s \n Dorohedoro : (2000) \n Hellsing : (2006)")

		elif c == "2010":
			print("Manga Books in 2010s \n Tokyo Ghoul : (2010) \n Blood on the Tracks : (2010)")

	elif b.lower() == "medium":
		c = input("Decade/s available With medium Horror books (1990s, 2020s) --> ")

		if c == "1990":
			print("Manga Books in 1990s \n  Hideshi Hino's Panorama of Hell : (1993) \n Elvira: Mistress of the Dark : (1995)")

		elif c == "2020":
			print("Manga Books in 2020s \n I Am a Hero : (2020) \n Barefoot Gen : (2020)")

	elif b.lower() == "long":
		c = input("Decade/s available with Long Horror books (1980s, 1970s) --> ")

		if c == "1980":
			print("Manga Books in 1980s \n Kazuo Umezu's Drifting Classroom : (1980) \n Junji Ito's Gyo : (1984)")
		elif c == "1970":
			print("Manga Books in 1970s \n  Eko Eko Azarak : (1975) \n Violence Jack : (1970)")

elif a == "romance":
	b = input("How long Manga should be? (Short/Medium/Long) --> ")
	if b.lower() == "short":
		c = input("Decade/s With short Romance books (2000s, 2010s) --> ")

		if c == "2000":
			print("Manga Books in 2000s \n Nana (Ai Yazawa) : (2000) \n Honey and Clover (Chica Umino) : (2000)")

		elif c == "2010":
			print("Manga Books in 2010s \n Kamikamikaeshi : (2010) \n Ane no Kekkon (My Sister’s Marriage) : (2010)")

	elif b.lower() == "medium":
		c = input("Decade/s available With medium Romance books (1990s, 2020s) --> ")

		if c == "1990":
			print("Manga Books in 1990s \n  Itazura na Kiss : (1990) \n Amai Seikatsu : (1995)")

		elif c == "2020":
			print("Manga Books in 2020s \n New Normal by Akito Aihara : (2020) \n 200 m Saki no Netsu by Miyoshi Tomori : (2020)")

	elif b.lower() == "long":
		c = input("Decade/s available with Long Romance books (1980s, 1970s) --> ")

		if c == "1980":
			print("Manga Books in 1980s \n Maison Ikkoku : (1980) \n P.S. Genki Desu, Shunpei : (1980)")
		elif c == "1970":
			print("Manga Books in 1970s \n  The Rose of Versailles : (1970) \n From Eroica with Love : (1970)")

else :
	print("Invalid Input")
