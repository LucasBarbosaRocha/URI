import random
def criaMatriz(lin,col):
	A = []
	for i in range(lin):
		linha = []
		for j in range(col):
			linha = linha + [random.randint(1,10)]
		A = A +[linha]
	return A

while True:
	try:
		number = int(raw_input())

		matriz = criaMatriz(number, number)
		ini = 0
		fim = number-1

		for i in range(number):
			msg = ""
			for j in range(number):
				matriz[i][j] = 3
				matriz[i][ini] = 1
				matriz[i][fim] = 2
				msg = msg + str(matriz[i][j])
			print msg
			msg = ""
			ini = ini + 1
			fim = fim - 1
	except:
		break

