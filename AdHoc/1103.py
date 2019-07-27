while True:
	entrada = input().split(" ")
	h1 = int(entrada[0])
	m1 = int(entrada[1])
	h2 = int(entrada[2])
	m2 = int(entrada[3])
	horas = 0
	minutos = 0

	if (h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0):
		break

	if (h1 == h2):
		if (m1 > m2):
			horas = (24 - h1) + h2
	else:
		if (h1 < h2):
			horas = h2 - h1
		else:
			horas = 24 - abs(h2 - h1)

	if (m1 <= m2):
		minutos = m2 - m1
		total = horas*60 + minutos
	else:
		minutos = m1 - m2
		total = horas*60 - minutos

	print (total)