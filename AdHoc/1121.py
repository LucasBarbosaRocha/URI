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

	j = col+1
	ast = 0
	if j < limiteC and (m[lin][j] == '.' or m[lin][j] == '*'):
		if m[lin][j] == '*':
			ast = ast  +1
		m[lin][j] = '.'
		col = col + 1
		j = j + 1
	qtd = [col, ast]
	return qtd


def paraEsquerda(m, lin, col):

	j = col-1
	ast = 0
	if j >= 0 and (m[lin][j] == '.' or m[lin][j] == '*'):
		if m[lin][j] == '*':
			ast = ast  +1	
		m[lin][j] = '.'			
		col = col - 1
		j = j - 1
	qtd = [col, ast]
	return qtd

def paraCima(m, lin, col):
	j = lin-1
	ast = 0
	if j >= 0 and (m[j][col] == '.' or m[j][col] == '*'):
		if m[j][col] == '*':
			ast = ast + 1		
		m[j][col] = '.'			
		lin = lin - 1
		j = j - 1
	qtd = [lin, ast]
	return qtd

def paraBaixo(m, lin, col, limiteL):
	j = lin+1
	ast = 0

	if j < limiteL and (m[j][col] == '.' or m[j][col] == '*'):
		if m[j][col] == '*':
			ast = ast + 1			
		m[j][col] = '.'			 			
		lin = lin + 1
		j = j + 1
	qtd = [lin, ast]
	return qtd

entrada = raw_input().split(" ")
lin = int(entrada[0])
col = int(entrada[1])
ins = int(entrada[2])

iIni = 0
jIni = 0
oriIni = ""

while lin != 0 and col != 0 and ins != 0:
	m = criaMatriz(lin, col)
	for i in range(lin):
		aux = raw_input()
		for j in range(col):
			m[i][j] = aux[j]
			if m[i][j] == 'N':
				bkpI = iIni = i
				bkpJ = jIni = j
				oriIni = 'N'
			elif m[i][j] == 'S':
				bkpI = iIni = i
				bkpJ = jIni = j
				oriIni = 'S'
			elif m[i][j] == 'L':
				bkpI = iIni = i
				bkpJ = jIni = j
				oriIni = 'L'
			elif m[i][j] == 'O':
				bkpI = iIni = i
				bkpJ = jIni = j
				oriIni = 'O'
	comandos = raw_input()

	figurinhas = 0
	for i in range(ins):
			if comandos[i] == 'F':
				if oriIni == 'N':
					qtd = paraCima(m, iIni, jIni)
					iIni = qtd[0]
					figurinhas = figurinhas + qtd[1]
				elif oriIni == 'S':
					qtd = paraBaixo(m, iIni, jIni, lin)
					iIni = qtd[0]
					figurinhas = figurinhas + qtd[1]
				elif oriIni == 'L':
					qtd = paraDireita(m, iIni, jIni, col)
					jIni = qtd[0]
					figurinhas = figurinhas + qtd[1]
				elif oriIni == 'O':
					qtd = paraEsquerda(m, iIni, jIni)
					jIni = qtd[0]
					figurinhas = figurinhas + qtd[1]
			elif comandos[i] == 'D':
				if oriIni == 'N':
					oriIni = 'L'
				elif oriIni == 'L':
					oriIni = 'S'
				elif oriIni == 'S':
					oriIni = 'O'
				elif oriIni == 'O':
					oriIni = 'N'
			elif comandos[i] == 'E':
				if oriIni == 'N':
					oriIni = 'O'
				elif oriIni == 'O':
					oriIni = 'S'
				elif oriIni == 'S':
					oriIni = 'L'
				elif oriIni == 'L':
					oriIni = 'N'	
			m[bkpI][bkpJ] = '.'		

	print figurinhas
	
	entrada = raw_input().split(" ")
	lin = int(entrada[0])
	col = int(entrada[1])
	ins = int(entrada[2])