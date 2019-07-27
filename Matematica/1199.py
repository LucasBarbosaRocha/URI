while True:
	entrada = input()
	teste = entrada[0]
	if (teste == '-'):
		break
	elif (len(entrada) > 2 and entrada[0:2] == "0x"):
		# Hexa to Dec
		valor = entrada[2:len(entrada)].upper()
		#print (valor)
		tam = len(valor)
		elevado = 0
		result = 0
		for i in range(tam - 1, -1, -1):
			if (valor[i] == 'A'):
				number = 10
			elif (valor[i] == 'B'):
				number = 11
			elif (valor[i] == 'C'):
				number = 12
			elif (valor[i] == 'D'):
				number = 13
			elif (valor[i] == 'E'):
				number = 14
			elif (valor[i] == 'F'):
				number = 15
			else:
				number = int(valor[i])
			result = result + (number * (16**elevado))
			elevado = elevado + 1
		print (result)
	else: 
	# Dec to Hexa
		print("0x%X" %int(entrada))