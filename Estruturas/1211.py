while True:
	try:		
		qtd = int(input())
		lista = []
		for i in range(qtd):
			num = (input())
			lista.append(num)
		lista.sort()
		#print (lista)
		cont = 0

		for i in range(1, qtd):
			n1 = lista[i-1]
			n2 = lista[i]
			#print (n1, n2)
			if (n1[0] == n2[0]):
				if (len(n1) > len(n2)):
					tam = len(n1)
				else:
					tam = len(n2)
				j = 0
				while (j < tam and n1[j] == n2[j]):
					cont = cont + 1					
					j = j + 1	
		print (cont)
	except:
		break
