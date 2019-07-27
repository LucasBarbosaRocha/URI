base = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]

def preencheVetor(fim, V):
	n = fim
	while n > 0:
		dig = n%10
		n = n/10
		V[dig] = V[dig] + 1
	return V

entrada = raw_input().split(" ")
ini = int(entrada[0])
fim = int(entrada[1])

while ini != 0 and fim != 0:
	v = [0,0,0,0,0,0,0,0,0,0]


	


	print v





	entrada = raw_input().split(" ")
	ini = int(entrada[0])
	fim = int(entrada[1])	