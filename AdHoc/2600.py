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

def repetidos(lista):
	aux = 1
	tam = len(lista)
	for i in range(tam):
		value = lista[i]
		for j in range(i+1, tam):
			if value == lista[j]:
				aux = 0
			if value == 0 or lista[j] == 0:
				aux = 0
	return aux


n = input()

for i in range(n):
	lista = []
	m = criaMatriz(3, 4)
	zeraMatriz(m, 3, 4)

	entrada = input()
	m[0][1] = entrada
	lista.append(m[0][1])
	entrada = raw_input().split(" ")
	for j in range(4):
		m[1][j] = int(entrada[j])
		lista.append(m[1][j])
	entrada = input()
	m[2][1] = entrada
	lista.append(m[2][1])

	if repetidos(lista) == 0:
		print "NAO"
	else:
		if (m[0][1] + m[2][1]) == 7 and (m[1][0] + m[1][2]) == 7 and (m[1][1] + m[1][3]) == 7:
			print "SIM"
		else:
			print "NAO"