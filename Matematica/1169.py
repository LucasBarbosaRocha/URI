kCasos = int(raw_input())

while kCasos > 0:
	casasDoTabuleiro = int(raw_input())
	qtdGraos = 1
	for i in range(1,casasDoTabuleiro):
		qtdGraos = qtdGraos + (2**i)
	# 12 graos conrrespondem a 1 grama
	gramas = (qtdGraos/12)
	quilos = (gramas/1000)
	print "%d kg" % quilos
	kCasos = kCasos - 1