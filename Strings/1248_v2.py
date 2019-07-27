N = int(input())
for i in range(N):
	dieta = input()
	cafe = input()
	almoco = input()
	janta = ""
	refeicao = cafe + almoco
	dietaOrdenada = sorted(dieta)
	refeicaoOrdenada = sorted(refeicao)
	#print(dietaOrdenada, refeicaoOrdenada)
	if (len(refeicaoOrdenada) > len(dietaOrdenada)):
		print("CHEATER")
	else:
		aux = 1
		j = 0

		for i in range(len(refeicaoOrdenada)):
			if (refeicaoOrdenada[i] not in dietaOrdenada):
				aux = 0
				break

		if (aux == 1):
			for i in range(len(dietaOrdenada)):
				if (refeicaoOrdenada.count(dietaOrdenada[i]) == 0):
					janta = janta + dietaOrdenada[i]
				elif ((refeicaoOrdenada.count(dietaOrdenada[i]) > 1)):
					aux = 0
					break
		if (aux == 1):
			print (janta)
		else:
			print ("CHEATER")

