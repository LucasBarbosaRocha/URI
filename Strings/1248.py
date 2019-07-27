n = int(input())
while n > 0:
	dieta  = input()
	cafe   = input()
	almoco = input()

	comida = cafe + almoco

	dietaList  = []
	comidaList = []
	comer = ""

	tamDieta = len(dieta)

	for i in range(tamDieta):
		dietaList.append(dieta[i])

	tamComida = len(comida)
	for i in range(tamComida):
		comidaList.append(comida[i])
	#dietaList.sort()
	dietaList = sorted(set(dietaList))
	comidaList.sort()
	#comidaList = sorted(set(comidaList))
	#print (dietaList)
	#print (comidaList)

	v = i = j = 0
	while (i < tamComida and j < tamDieta):

		if (dietaList[j] > comidaList[i]):
			v = 1
			break
		elif (dietaList[j] < comidaList[i]):
			comer = comer + dietaList[j]
			del(dietaList[j])
		else:
			del(dietaList[j])
			del(comidaList[i])
			tamDieta  = tamDieta  - 1
			tamComida = tamComida - 1

	if (len(comidaList) > 0 or v == 1):
		print("CHEATER")
	else:
		if (j < len(dietaList)):
			for i in range(len(dietaList)):
				comer = comer + dietaList[i]
		if (v == 0):
			print(comer)
	n = n - 1