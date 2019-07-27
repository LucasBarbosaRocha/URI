while True:
	try:
		n = int(raw_input())
		lista = []
		for i in range(n):
			entrada = raw_input().split(" ")
			ini = int(entrada[0])
			fim = int(entrada[1])
			j = ini
			while j <= fim:
				lista.append(j)
				j = j + 1
		p = int(raw_input())
		if (p in lista):			
			lista.sort()
			#print(lista, p)
			i = 0
			while (i < len(lista) and lista[i] != p):
				i = i + 1
			ini = i
			i = ini
			while (i < len(lista) and lista[i] == p):
				i = i + 1
			fim = i
			print("%d found from %ld to %ld" %(p, ini, fim - 1))
		else:
			print("%d not found" %p)
	except:
		break