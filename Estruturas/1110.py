while True:
	n = int(input())
	if (n == 0):
		break
	# Topo eh a primeira posição

	lista = [0]*(n)
	tam = len(lista)
	removidos = []
	for i in range(tam):
		lista[i] = (i + 1)

	while (len(lista) > 1):
		removidos.append(lista[0])
		del lista[0]
		lista.append(lista[0])
		del lista[0]
	#print (removidos)
	#print (lista)
	tamRemovidos = len(removidos)
	resultado = "Discarded cards:"
	for i in range(tamRemovidos):
		if (i == 0):
			resultado = resultado + " " + str(removidos[i])
		elif (i < tamRemovidos -1):
			resultado = resultado + ", " + str(removidos[i])
		else:
			resultado = resultado + ", " +  str(removidos[i])
	print (resultado)
	print ("Remaining card: %s" %lista[0])