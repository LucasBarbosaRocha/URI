n = int(input())
for i in range(n):
	tam = int(input())
	entrada = input()
	bkp = list(entrada)
	entradaList = list(entrada)
	tamList = len(entradaList)
	maiores = 0
	for j in range(tamList):
		palavra = entradaList[j]
		#print ("1 %s" %palavra)
		for k in range(j + 1, tamList):
			if (palavra > entradaList[k]):
				aux = entradaList[k]
				entradaList[k] = palavra
				palavra = aux

		entradaList[j] = palavra
		#print ("2 %s" %palavra)
	#print(bkp)
	#print(entradaList)
	trocas = 0
	for j in range(tamList):
		if (bkp[j] != entradaList[j]):
			trocas = trocas + 1
	#print (trocas)
	if (trocas == 2):
		print("There are the chance.")
	else:
		print("There aren't the chance.")