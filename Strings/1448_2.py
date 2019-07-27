n = int(input())
i = 0
while i < n:
	frase = raw_input()
	time1 = raw_input()
	time2 = raw_input()
	tam = len(frase)
	pontos1 = 0
	pontos2 = 0
	empate = 0
	vence = ""

	for j in range(tam):
		letra = frase[j]
		if (empate == 0):
			valor = 0
			if (j < len(time1) and j < len(time2) and letra == time1[j] and letra != time2[j]):
				empate = 1
			elif(j < len(time1) and j < len(time2) and letra != time1[j] and letra == time2[j]):
				empate = 2
	for j in range(tam):
		letra = frase[j]
		if (j < len(time1) and letra == time1[j]):
			pontos1 = pontos1 + 1
		if (j < len(time2) and letra == time2[j]):
			pontos2 = pontos2 + 1

	if (pontos2 > pontos1):
		vence = '2'
	elif(pontos2 < pontos1):
		vence = '1'
	else :
		if (empate == 1):
			vence = '1'
		elif(empate == 2):
			vence = '2'
		else:
			vence = '0'

	print("Instancia %d" % (i + 1))
	if (vence == '0'):
		print("empate")
	else :
		print("time %s" % vence)
	print 
	i = i + 1