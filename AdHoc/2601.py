import random

def criaMatriz(lin,col):
    A = []
    for i in range(lin):
        linha = []
        for j in range(col):
            linha = linha + [random.randint(1,10)]
        A = A +[linha]
    return A

def zeraMatriz(m, lin, col):

	for i in range(lin):
		for j in range(col):
			m[i][j] = 0

n = input()

for i in range(n):
	lista = []
	v = [1,2,3,4,5,6]
	m = criaMatriz(3, 4)
	zeraMatriz(m, 3, 4)

	entrada = raw_input()
	m[0][1] = entrada
	lista.append(m[0][1])
	if m[0][1] != '*':
		v[int(m[0][1])-1] = -1
	entrada = raw_input().split(" ")
	for j in range(4):
		m[1][j] = entrada[j]
		if m[1][j] != '*':
			v[int(m[1][j])-1] = -1
		lista.append(m[1][j])
	entrada = raw_input()
	m[2][1] = entrada
	lista.append(m[2][1])
	if m[2][1] != '*':
		v[int(m[2][1])-1] = -1

	print v

