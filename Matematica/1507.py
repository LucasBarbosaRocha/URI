n = int(input())
for i in range(n):
	sequencia = input()
	q = int(input())
	for j in range(q):
		entrada = input()
		tam = len(entrada)
		v = 0
		tamS = len(sequencia)
		pos = 0
		bkp = sequencia
		posAnterior = 0
		a = [0]*tam
		past = 0
		first = 1
		#print("------------")
		while (v < tam):
			f = bkp[pos:].find(entrada[v])
			#print (f)
			if (f != -1):
				#print(past, f)
				if (first == 1):
					a[v] = past + f
					past = past + f
					first = 0
				else:
					a[v] = past + f + 1
					past = past + f + 1
				pos = past + 1
				v = v + 1
			else :
				break
		val = 1
		#print (a)
		for k in range(tam-1):
			if (a[k] >= a[k+1]):
				val = 0
				break

		if (val == 1):
			print("Yes")
		else:
			print ("No")