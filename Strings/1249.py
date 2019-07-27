while True:
	try:
		entrada  = input()
		tam      = len(entrada)
		resposta = ""

		i = 0
		while (i < tam):
			letra = entrada[i]
			#print(letra, letra.isalpha())
			if (letra.isalpha()):
				if (letra.isupper()):
					if (ord(letra) + 13 <= 90):
						letra = chr(ord(letra) + 13)
					else:
						letra = chr(65 + (12 - (90 - ord(letra))))
				else:
					if (ord(letra) + 13 <= 122):
						letra = chr(ord(letra) + 13)
					else:
						letra = chr(97 + (12 - (122 - ord(letra))))
			resposta = resposta + letra
			i = i + 1
		print(resposta)
	except :
		break