import random

def criaMatriz(lin, col):
	A = []
	for i in range(lin):
		linha = []
		for j in range(col):
			linha = linha + [random.randint(1,10)]
		A = A +[linha]
	return A

def imprime(m, lin, col):
	for i in range(lin):
		linha = ""
		for j in range(col):
			linha = linha + m[i][j]
		print (linha)
	print("@")


while True:
	try:
		n = int(input())
		m = criaMatriz(n, n)

		for i in range(n):
			for j in range(n):
				m[i][j] = 'O'

		if (n == 0):
			break

		if (n != 1):
			meio = n - 2
		else:
			meio = 0

		m[meio][meio] = 'X'

		imprime(m, n, n)



	except :
		break