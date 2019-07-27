while True:
	try:

		entrada = input()
		tam = len(entrada)
		resposta = ""

		i = 0
		isS = 1
		isB = 1
		while i < tam:
			if (entrada[i] == '_'):
				if (isS):
					resposta = resposta + "<i>"
					isS = 0
				else:
					resposta = resposta + "</i>"
					isS = 1
			elif (entrada[i] == '*'):
				if (isB):
					resposta = resposta + "<b>"
					isB = 0
				else:
					resposta = resposta + "</b>"
					isB = 1
			else:
				resposta = resposta + entrada[i]
			i = i + 1
		print (resposta)
	except :
		break