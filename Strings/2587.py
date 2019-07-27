n = int(input())

while (n > 0):
	palavra1 = input()
	palavra2 = input()
	pIncompl = input()
	tam = len(palavra1)

	i = 0
	letras1 = []
	letras2 = []
	while (i < tam):
		if(pIncompl[i] == '_'):
			#print ("teste")
			if (palavra1[i] not in letras1):
				letras1.append(palavra1[i])
			if (palavra2[i] not in letras2):
				letras2.append(palavra2[i])
		i = i + 1
	#print (letras1, letras2)
	tam = len(letras1)
	i = 0
	v = 1
	while (i < tam):
		letra = letras1[i]
		v = 1
		j = 0
		while (j < tam):
			if (i != j and letra != letras2[j]):
				v = 0
			j = j + 1
		if (v == 1):
			break
		i = i + 1


	if (v == 1):
		print ("Y")
	else :
		print ("N")

	n = n - 1