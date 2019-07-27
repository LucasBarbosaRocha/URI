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

cont = 0
if letra == 'S':
	soma = 0
	for i in range(11,-1,-1):
		for j in range(cont+1,12-(cont+1)):
			soma = soma + matriz[i][j]
		cont = cont + 1
	print soma
else:
	mult = 1
	for i in range(11,-1,-1):
		for j in range(cont+1,12-(cont+1)):
			mult = mult * matriz[i][j]
			cont = cont + 1
	print mult
