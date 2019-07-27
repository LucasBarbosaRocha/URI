def criaMatriz(lin, col):
	A = []
	for i in range(lin):
		linha = []
		for i in range(col):
			linha = linha + [0]
		A = A + [linha]
	return A

while True:
	cavalo = input()
	if (len(cavalo) > 0 and cavalo[0] == '0'):
		break
	peoes = []
	for i in range(8):
		peao = input()
		peoes.append(peao)
	print (cavalo, peoes)
	matriz = criaMatriz(8, 8)

	peoesOficiais = []
	for i in range(8):
		peao = peoes[i]
		linha = int(peao[0])
		if (peao[1] == 'a'):
			coluna = 1
		elif (peao[1] == 'b'):
			coluna = 2
		elif (peao[1] == 'c'):
			coluna = 3
		elif (peao[1] == 'd'):
			coluna = 4
		elif (peao[1] == 'e'):
			coluna = 5
		elif (peao[1] == 'f'):
			coluna = 6
		elif (peao[1] == 'g'):
			coluna = 7
		elif (peao[1] == 'h'):
			coluna = 8
		matriz[linha][coluna] = 1
		va = str(linha) + str(coluna)
		peoesOficiais.append(va)
	linha = int(cavalo[0])
	if (cavalo[1] == 'a'):
		coluna = 1
	elif (cavalo[1] == 'b'):
		coluna = 2
	elif (cavalo[1] == 'c'):
		coluna = 3
	elif (cavalo[1] == 'd'):
		coluna = 4
	elif (cavalo[1] == 'e'):
		coluna = 5
	elif (cavalo[1] == 'f'):
		coluna = 6
	elif (cavalo[1] == 'g'):
		coluna = 7
	elif (cavalo[1] == 'h'):
		coluna = 8
	matriz[linha][coluna] = 2
	cavaloOficial = str(linha)+str(coluna)
	print(matriz)
	print(peoesOficiais)
	print(cavaloOficial)

	for i in range(8):
		
