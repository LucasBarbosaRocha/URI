import random

def criaMatriz(lin,col):
	A = []
	for i in range(lin):
		linha = []
		for j in range(col):
			linha = linha + [random.randint(1,10)]
		A = A +[linha]
	return A

def soma(matriz, lin, col):
	s = 0
	for j in range(col):
		s = s + matriz[lin][j]
	return s

def multi(matriz, lin, col):
	m = 1
	for j in range(col):
		m = m * matriz[lin][j]	
	return m

number = int(raw_input())
char = raw_input()
l = c = 11
matriz = criaMatriz(l,c)

for i in range(l):
	for j in range(c):
		matriz[i][j] = float(raw_input())

if str(char) == 'S':
	print "%.1f" % soma(matriz,number,c)
elif str(char) == 'M':
	print "%.1f" % multi(matriz,number,c)