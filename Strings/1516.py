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

	entrada = input().split(" ")
	n = int(entrada[0])
	m = int(entrada[1])

	if (n == 0 and m == 0):
		break

	matriz = criaMatriz(n,m)
	for i in range(n):
		linha = input()
		tam = len(linha)
		for j in range(tam):
			print
			matriz[i][j] = linha[j]

	entrada2 = input().split(" ")
	a = int(entrada2[0])
	b = int(entrada2[1])

	qtdLinhas = int((a - n) / n)
	qtdColunas = int(b / m)

	for i in range(n):
		linha = ""
		for j in range(m):
			for k in range(qtdColunas):
				linha = linha + matriz[i][j]
		print (linha)

		for j in range(qtdLinhas):
			print (linha)
	print ()