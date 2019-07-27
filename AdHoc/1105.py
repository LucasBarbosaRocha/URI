while True:
	entrada = input().split(" ")
	B = int(entrada[0])
	N = int(entrada[1])
	if (B == 0 and N == 0):
		break
	entrada = input().split(" ")
	bancos = [0]*B
	for i in range(len(entrada)):
		bancos[i] = int(entrada[i])
	#print (bancos)
	for i in range(N):
		entrada = input().split(" ")
		b = int(entrada[0]) - 1
		c = int(entrada[1]) - 1
		v = int(entrada[2])
		bancos[c] = bancos[c] + v
		bancos[b] = bancos[b] - v
		#print(bancos)
	aux = 1
	for i in range(len(bancos)):
		if (bancos[i] < 0):
			aux = 0
	if (aux == 0):
		print("N")
	else:
		print("S")