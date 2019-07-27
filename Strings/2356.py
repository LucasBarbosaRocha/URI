while True:
	try:	
		dna = input()
		marcador = input()
		val = 0
		i = 0
		while i < len(dna):
			tam = 0
			j = 0
			ii = i
			while ii < len(dna) and j < len(marcador):
				if (dna[ii] == marcador[j]):
					tam = tam + 1	
				ii = ii + 1
				j = j + 1	
			if (tam == len(marcador)):
				val = 1
				break
			i = i + 1

		if (val == 1):
			print("Resistente")
		else:
			print("Nao resistente")
	except :
		break
			
