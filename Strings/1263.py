while True:

	try:
		entrada    = input()
		entrada    = entrada.upper()
		entrada    = entrada.split(" ")
		tam        = len(entrada)
		aliteracao = 0
		palavra    = entrada[0]
		i          = 1
		#print(entrada)
		while (i < tam):
			v = 1
			palavra2 = entrada[i]
			while (palavra2 == ''): # Ignorar espaços em branco
				del(entrada[i])
				tam = tam - 1
				palavra2 = entrada[i]

			if (palavra[0] == palavra2[0]):
				aliteracao = aliteracao + 1
				i = i + 1
				if (i < tam):
					palavra = entrada[i]
					while (palavra == ''): # Ignorar espaços em branco
						del(entrada[i])
						tam = tam - 1
						palavra = entrada[i]					
					i = i + 1
					v = 0
					while (i < tam and palavra[0] == palavra2[0]):
						palavra = entrada[i]
						while (palavra == ''):  # Ignorar espaços em branco
							del(entrada[i])
							tam = tam - 1
							palavra = entrada[i]	
						i = i + 1
			else:
				palavra = palavra2

			if (v == 1):
				i = i + 1

		print (aliteracao)
	except :
		break