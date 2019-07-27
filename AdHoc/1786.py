while True:
	try:
		entrada = input()
		aux = 0	
		for i in range(len(entrada)):
			aux = aux + int(entrada[i])*(i+1)
		resto = aux%11
		b1 = 0
		if (resto == 10):
			b1 = 0
		else:
			b1 = resto

		aux = 0
		for i in range(len(entrada)):
			aux = aux + int(entrada[i])*(len(entrada)-i)
		resto = aux%11
		b2 = 0
		if (resto == 10):
			b2 = 0
		else:
			b2 = resto

		#print(b1, b2)

		resp = entrada[0:3] + "." + entrada[3:6] + "." + entrada[6:9] + "-" + str(b1) + str(b2)
		print (resp)

	except:
		break