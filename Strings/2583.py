C = int(input())
for i in range(C):
	N = int(input())
	coisas = []
	for j in range(N):
		entrada = input().split(" ")
		if (entrada[1] == 'chirrion'):
			if (entrada[0] in coisas):
				coisas.remove(entrada[0])
		elif (entrada[1] == 'chirrin'):
			if (entrada[0] not in coisas):
				coisas.append(entrada[0])
	print("TOTAL")
	coisas.sort()
	for j in range(len(coisas)):
		print(coisas[j])

