while True:
	entrada = input().split(" ")
	if (entrada[0] == '0' and entrada[1] == '0'):
		break

	a = 1 # 1 Ninguém resolveu todos os problemas.
	b = 1 # Todo problema foi resolvido por pelo menos uma pessoa (não necessariamente a mesma).
	c = 1 # Não há nenhum problema resolvido por todos.
	d = 1 # Todos resolveram ao menos um problema (não necessariamente o mesmo).
	qtdEx = int(entrada[1])
	problemasB = [1]*qtdEx
	problemasC = [0]*qtdEx
	pessoas = int(entrada[0])
	for i in range(pessoas):
		jogador = input().split(" ")
		qtdD = 0
		qtdA = 0
		for j in range(len(jogador)):
			if (jogador[j] == '0'):
				qtdD = qtdD + 1
			if (jogador[j] == '1'):
				qtdA = qtdA + 1

			if (jogador[j] == '0'):
				problemasB[j] = 0

			if (jogador[j] == '1'):
				problemasC[j] = problemasC[j] + 1


		if (qtdD == qtdEx):
			d = 0
		#print(qtdA, qtdEx)
		if (qtdA == qtdEx):
			a = 0

	for i in range(len(problemasB)):
		if (problemasB[i] == 0):
			b = 0

	for i in range(len(problemasC)):
		#print(problemasC[i])
		if (problemasC[i] == pessoas):
			c = 0

	#print(a,b,c,d)
	print(a+b+c+d)