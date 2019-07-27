while True:
	entrada = input().split(" ")
	B = int(entrada[0])
	N = int(entrada[1])
	if (B == 0 and N == 0):
		break
	entrada = input().split(" ")
	bolas = [0]*(B+1)
	bolasValidas = [0]*(B+1)
	for i in range(len(entrada)):
		aux = int(entrada[i])
		bolas[aux] = 1
	#print(bolas)
	for i in range(len(bolas)):
		for j in range(len(bolas)-1,i,-1):
			if (bolas[j] == 1 and bolas[i] == 1):
				pos = j - i
				bolasValidas[pos] = 1
	aux = 1
	#print(bolasValidas)
	for i in range(1,len(bolasValidas)):
		if (bolasValidas[i] == 0):
			aux = 0
			break
	if (aux == 1):
		print("Y")
	else:
		print("N")

