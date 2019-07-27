while True:
	try:
		n = int(input())

		if (n == 0):
			break

		lista = []
		while (n > 0):
			nome = input()
			tamanho = input().split(" ")
			va = nome, tamanho
			lista.append(va)
			n = n - 1
		# Ordenando por cor (crescente)
		lista = sorted(lista,  key=lambda x: x[1][0])
		listaBKP = []
		print (lista)
		print ()

		tam = len(lista)
		cor = lista[0][1][0]
		i = 1
		# Ordenando por tamanho (Decrescente) e nome (crescente)
		while (i < tam):
			while (lista[i][1][0] == cor):
				listaBKP.append(lista[i])
				i = i + 1
			# Ordenando por tamanho a mesma cor
			listaBKP = sorted(listaBKP, key=lambda x: x[1][1])
			tam2 = len(listaBKP)
			listaBKP2 = []
			# para cada tamanho ordenar por nome
			tamanho = listaBKP[0][0]
			j = 1
			while (j < tam2):
				while (listaBKP[j][1][1] == tamanho):
					listaBKP2.append(listaBKP[j])
					j = j + 1
				listaBKP2 = sorted(listaBKP2, key=lambda x: x[0])
				tam3 = len(listaBKP2)
				for k in range(tam3):
					print ("%s %s %s", listaBKP2[k][1][0], listaBKP2[k][1][1], listaBKP2[k][0])
	except :
		break