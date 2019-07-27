while True:
	try:
		entrada = input().split("+")
		valores = []
		valores.append(entrada[0])
		entrada = entrada[1].split("=")
		valores.append(entrada[0])
		valores.append(entrada[1])
		#print (valores)
		result = 0
		if (valores[0].isdigit() and valores[1].isdigit()):
			result = int(valores[0]) + int(valores[1])
		elif (valores[0].isdigit() and valores[2].isdigit()):
			valor = int(valores[0]) * -1
			result = valor + int(valores[2])
		elif (valores[1].isdigit() and valores[2].isdigit()):
			valor = int(valores[1]) * -1
			result = valor + int(valores[2])
		print(result)

	except :
		break