import random

def criaMatriz(lin,col):
	A = []
	for i in range(lin):
		linha = []
		for j in range(col):
			linha = linha + [random.randint(1,10)]
		A = A +[linha]
	return A

def LCS(p1, p2, m1, m2):
	c = criaMatriz(m1, m2)
	for i in range(m1):
		c[i][0] = 0	
	for i in range(m2):
		c[0][i] = 0
	for i in range(1, m1):
		for j in range(1, m2):
			if(p1[i] == p2[j]):
				c[i][j] = c[i-1][j-1] + 1
			elif c[i-1][j] >= c[i][j-1]:
				c[i][j] = c[i-1][j]
			else:
				c[i][j] = c[i][j-1]
	#print(c)
	return c[m1-1][m2-1]

while True:
	try:
		p1 = input()
		p1 = " " + p1
		p2 = input()
		p2 = " " + p2
		m1 = len(p1)
		m2 = len(p2)
		resposta = LCS(p1, p2, m1, m2)
		print(resposta)
	except :
		break




	