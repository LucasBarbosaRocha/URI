while True:
	try:
		entrada = input()
		tam = len(entrada)

		entrada2 = ""
		for i in range(tam):
			entrada2 = entrada2 + entrada[i]
			if (i < tam - 1):
				entrada2 = entrada2 + " "
		i = 1
		tam2 = len(entrada2)
		print (entrada2)
		espacos = " "
		while (i < tam):
			#print (i, tam, tam2)
			i = i + 1
			tam2 = tam2 - 2
			entrada2 = entrada2[:tam2]
			print("%s%s" %(espacos,entrada2))
			espacos = espacos + " "

		print()
	except :
		break