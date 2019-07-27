while True:
	try:
		entrada = raw_input().split(" ")
		palavras = int(entrada[0])
		linhas = int(entrada[1])
		caracteres = int(entrada[2])

		v = raw_input().split(" ")

		tam = 0
		cont = 0
		paginas = 0
		pal = 0
		li = 0

		for i in range(palavras):
			tam = tam + len(v[i])
			if tam == caracteres:
				tam = 0
				li = li + 1
			elif tam  > caracteres:
				tam = len(v[i]) + 1
				li = li + 1
			elif i < palavras:
				tam = tam + 1

				if tam == caracteres:
					tam = 0
					li = li + 1
			if li == linhas:
				li = 0
				paginas = paginas + 1

		if tam > 0 or li > 0:
			paginas = paginas + 1
		print paginas
	except :
		break