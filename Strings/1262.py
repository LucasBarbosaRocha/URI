while True:
	try:
		entrada = input()
		n = int(input())
		tam = len(entrada)
		p = 0
		i = 0
		while (i < tam):
			if (entrada[i] == 'W'):
				i = i + 1
				p = p + 1
			elif (entrada[i] == 'R'):
				p = p + 1
				qtd = 0
				while (qtd < n and i < tam and entrada[i] == 'R'):
					i = i + 1
					qtd = qtd + 1
		print(p)
	except :			
		break