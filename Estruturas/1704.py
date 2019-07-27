def esq(i):
	return 2*(i)+1

def dire(i):
	return (2*i)+2

def desc(S, i, n):
	e = esq(i)
	d = dire(i)
	if e < n and S[e] > S[i]:
		maior = e
	else:
		maior = i
	if d < n and S[d] > S[maior]:
		maior = d
	if (i != maior):
		aux = S[i]
		S[i] = S[maior]
		S[maior] = aux
		desc(S, maior, n)

def constroiMaxHeap(S):
	n = len(S)
	for i in range(int(n/2) - 1, -1, -1):
		desc(S, i, len(S))

def heapSort(S):
	n = len(S)
	constroiMaxHeap(S)
	for i in range(n-1, 0, -1):
		aux = S[0]
		S[0] = S[i]
		S[i] = aux
		n = n - 1
		desc(S, 0, n)

def resolve(S, validos, H):
	maior = S[0]
	usados = 0
	print ("--------------")
	for i in range(H+1):
		print (lista)
		if (maior[1] >= (i+1)):
			usados = usados + 1
			validos[maior[1]] = validos[maior[1]] + 1
			S[0][0] = S[len(S)-1][0]
			S[0][1] = S[len(S)-1][1]
			S.remove(maior)
			if (len(S) == 0):
				break
			desc(S, 0, len(S))
			maior = S[0]

	print ("====")
	print (lista)
	print ("USADOS %d < %d" %(usados, H))
	if (S != [] and usados < H):
		print (validos)
		# Ajustes
		for i in range(1, len(validos)):
			print (validos[i], i)
			if (validos[i] > i):
				validos[i-1] = 0

		# Removendo extras 
		i = 0
		N = len(S)
		print (validos)
		while (i < N):
			aux = S[i]
			print (validos[aux[1]])
			if (validos[aux[1]] == 1):
				S.remove(aux)
				N = len(S)
			if (len(S) == 0):
				break
			print ("AQIO")
			i = i + 1

	# Calculando preju
	prejuizo = 0
	if (S != []):
		for i in range(len(S)):
			prejuizo = prejuizo + S[i][0]
	return prejuizo



if __name__ == '__main__':
	while True:
		try:
			entrada = input().split(" ")
			N = int(entrada[0])
			H = int(entrada[1])
			lista = []
			validos = [1]*(H+1)

			for i in range(N):
				entrada = input().split(" ")
				lista.append([int(entrada[0]), int(entrada[1])])

			print (lista)
			constroiMaxHeap(lista)
			print (lista)
			prejuizo = resolve(lista, validos, H)
			print ("OI")
			print (lista)
			print ("Repsosta %d" %prejuizo)


		except :
			break