n = int(input())
for i in range(n):
	qtdProdutosDisponiveis = int(input())
	produtosDisponiveis = {}
	for j in range(qtdProdutosDisponiveis):
		entrada = input().split(" ")
		produtosDisponiveis[entrada[0]] = float(entrada[1])
	qtdProdutosQuero = int(input())
	resultado = 0
	for j in range(qtdProdutosQuero):
		entrada = input().split(" ")
		if (entrada[0] in produtosDisponiveis):
			resultado = resultado + (int(entrada[1]) * (produtosDisponiveis[entrada[0]]))
	print ("R$ %.2f" %resultado)