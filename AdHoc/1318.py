while True:
	entrada = input().split(" ")
	n = int(entrada[0])
	m = int(entrada[1])

	if (n == 0 and m == 0):
		break
	else:
		lista = input().split(" ")
		numeros = [0]*10000

		for i in range(m):
			numeros[int(lista[i])] = numeros[int(lista[i])] + 1
		qtd = 0
		for i in range(len(numeros)):
			if numeros[i] > 1:
				qtd = qtd + 1
		print (qtd)