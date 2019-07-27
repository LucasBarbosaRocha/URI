import random
def criaMatriz(lin,col):
	A = []
	for i in range(lin):
		linha = []
		for j in range(col):
			linha = linha + [random.randint(1,10)]
		A = A +[linha]
	return A

matriz = criaMatriz(12,12)
letra = raw_input()

for i in range(12):
	for j in range(12):
		matriz[i][j] = float(raw_input())


if letra == 'S':
	soma = 0
	for i in range(12):
		for j in range(i+1,12-(i+1)):
			soma = soma + matriz[i][j]
	print soma
else:
	mult = 1
	for i in range(12):
		for j in range(i+1,12-(i+1)):
			mult = mult * matriz[i][j]
	print mult
