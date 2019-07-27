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
	number = int(raw_input())
	ini = 1
	cont = 1
	if number == 0:
		break

	matriz = criaMatriz(number,number)

	for i in range(number):
		for j in range(number):
			matriz[i][j] = cont
			cont = cont*2
		cont = ini * 2
		ini = cont

	msg = ""
	for i in range(number):
		for j in range(number):			
			msg = msg + " " + str(matriz[i][j])
		print msg
		msg = ""
	print ""