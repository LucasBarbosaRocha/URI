def compara(frase, time1, time2):
	tam = len(frase)
	vence = ""
	empate = 0
	pontos1 = 0
	pontos2 = 0

	# Empates
	i = 0
	while (i < tam):
		letra = frase[i]
		if (empate == 0):
			if (i < len(time1) and i < len(time2) and letra == time1[i] and letra != time2[i]):
				empate = 1
			elif (i < len(time1) and i < len(time2) and letra != time1[i] and letra == time2[i]):
				empate = 2
		else:
			break
		i = i + 1
	# Pontos
	i = 0
	while (i < tam):
		letra = frase[i]
		if (i < len(time1) and letra == time1[i]):
			pontos1 = pontos1 + 1
		if (i < len(time2) and letra == time2[i]):
			pontos2 = pontos2 + 1
		i = i + 1

	print (pontos2, pontos1)

	if (pontos2 > pontos1):
		vence = '2'
	elif (pontos2 < pontos1):
		vence = '1'
	else:
		if (empate == 1):
			vence = '1'
		elif (empate == 2):
			vence = '2'
		else:
			vence = '0'
	return vence

n = input()
newDigit = ""
for digit in n:
	if (digit.isdigit()):
		newDigit += digit
		newDigit = int(newDigit)

for i in range(newDigit):
	frase = input()
	time1 = input()
	time2 = input()

	qtd   = compara(frase, time1, time2)
	print ("Instancia %d" %(i+1))
	if (qtd == '0'):
		print("empate")
	else:
		print("time %s" %qtd)
	print()