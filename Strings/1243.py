while True:
	try:
		entrada = input().split(" ")
		tam = len(entrada)

		if (entrada[tam - 1] == ''):
			#print("entrei")
			del(entrada[tam - 1])
			tam = tam - 1
		#print(entrada)

		entradaModificada = []
		for i in range(tam):
			#print(i, tam, entrada[i])
			if (entrada[i].isalpha()):
				entradaModificada.append(entrada[i])

			elif (entrada[i] != ''):				
				palavra = entrada[i]
				tamPalavra = len(palavra)
				#print("AQUI %s %d" %(palavra, tamPalavra))
				if (palavra[tamPalavra - 1] == '.'):
					palavra = palavra[:tamPalavra - 1]

				if (palavra.isalpha()):
					entradaModificada.append(palavra)

		tamModificada = len(entradaModificada)
		somaTamPalavras = 0
		qtdPalavras = 0
		#print(entradaModificada)
		for i in range(tamModificada):
			#print(entradaModificada[i])
			somaTamPalavras = somaTamPalavras + len(entradaModificada[i])
			qtdPalavras = qtdPalavras + 1

		if (tamModificada > 0):
			somaTamPalavras = somaTamPalavras
			media = (int) (somaTamPalavras / tamModificada)

		#print(somaTamPalavras, tamModificada, media)
		if (somaTamPalavras == 0 or media <= 3):
			print ("250")
		elif (media >= 4 and media <= 5):
			print ("500")
		else:
			print ("1000")
	except :
		break