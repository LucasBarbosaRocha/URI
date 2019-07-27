nc = int(input())
for i in range(nc):
	entrada = input().split(" ")
	n = int(entrada[0])
	k = int(entrada[1])
	lista = [1]*n
	vivos = n
	pos = 0
	while vivos > 1:
		j = 0
		while j < k:
			while (lista[pos] == -1):
				pos = pos + 1
				if (pos == n):
					pos = 0
			pos = pos + 1
			if (pos == n):
				pos = 0			
			j = j + 1
		lista[pos - 1] = -1
		vivos = vivos - 1
		#print (lista)
	print ("Case %d: %d" %((i+1), lista.index(max(lista)) + 1))


