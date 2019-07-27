import random

def criaMatriz(lin,col):
    A = []
    for i in range(lin):
        linha = []
        for j in range(col):
            linha = linha + [random.randint(1,10)]
        A = A +[linha]
    return A

def paraDireita(m, lin, col, limiteC):

	j = col
	while j < limiteC and m[lin][j] == '.':
		col = col + 1
		m[lin][j] = 'p'
		j = j + 1
	return col


def paraEsquerda(m, lin, col):

	j = col
	while j >= 0 and m[lin][j] == '.':
		col = col - 1
		m[lin][j] = 'p'
		j = j - 1
	return col


def paraCima(m, lin, col):
	j = lin
	while j >= 0 and m[j][col] == '.':
		lin = lin - 1
		m[j][col] = 'p'
		j = j - 1
	return lin

def paraBaixo(m, lin, col, limiteL):
	j = lin
	while j < limiteL and m[j][col] == '.':
		lin = lin + 1
		m[j][col] = 'p'
		j = j + 1
	return lin

col = input()
lin = input()
m = criaMatriz(lin, col)

for i in range(lin):
	str = raw_input()
	for j in range(col):
		m[i][j] = str[j]

i = 0
j = 0

while True:
	if m[i][j] == 'p':
		print "!"
		break
	elif m[i][j] == '*':
		print "*"
		break
	elif m[i][j] == '>':
		m[i][j] = 'p'
		j = j  + 1

		if j == col: # Mudando a direcao
			j = 0

		aux = paraDireita(m, i, j, col)
		j = aux
		#print m[i][aux]
	elif m[i][j] == '<':	
		m[i][j] = 'p'
		j = j  - 1

		if j < 0:
			j = col - 1

		aux = paraEsquerda(m, i, j)
		j = aux
		#print m[i][aux]
	elif m[i][j] == 'v':	
		m[i][j] = 'p'
		i = i  + 1

		if i == lin:
			i = 0

		aux = paraBaixo(m, i, j, lin)
		i = aux
		#print m[aux][j]
	elif m[i][j] == '^':	
		m[i][j] = 'p'
		i = i  - 1

		if i < 0:
			i = lin - 1

		aux = paraCima(m, i, j)
		i = aux
		#print m[aux][j]