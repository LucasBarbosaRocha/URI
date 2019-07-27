while True:
	try:
		entrada = input()
		tam = len(entrada)
		resposta = ""
		i = 0
		# ASCII (- 32) para maiuscula
		if entrada[i] == ' ':
			resposta = resposta + entrada[i]
			i = i + 1
			while entrada[i] == ' ' and i < tam:
				resposta = resposta + entrada[i]
				i = i + 1

		if entrada[i] >= 'a' and entrada[i] <= 'z':
			resposta = resposta + chr(ord(entrada[i]) - 32)
			i = i + 1
		else:
			resposta = resposta + entrada[i]
			i = i + 1

		m = 1 # 1 eh verdade que agora eh minusculo
		while (i < tam):
			if (m == 1):
				if (entrada[i] >= 'A' and entrada[i] <= 'Z'):
					resposta = resposta + chr(ord(entrada[i]) + 32)
				elif (entrada[i] >= 'a' and entrada[i] <= 'z'):
					resposta = resposta + entrada[i]

				if (entrada[i] != ' '):
					m = 0
				else:
					resposta = resposta + entrada[i]
			else:
				if (entrada[i] >= 'a' and entrada[i] <= 'z'):
					resposta = resposta + chr(ord(entrada[i]) - 32)
				elif (entrada[i] >= 'A' and entrada[i] <= 'Z'):
					resposta = resposta + entrada[i]

				if (entrada[i] != ' '):
					m = 1
				else:
					resposta = resposta + entrada[i]
			i = i + 1

		print (resposta)
	except :
		break