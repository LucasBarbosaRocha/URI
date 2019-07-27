n = int(input())
for i in range(n):
	entrada = input().split(" ")
	
	#print(entrada)
	operador = entrada[1]
	resp = int(entrada[4])
	dif = 0
	if (operador == '+'):
		n1 = int(entrada[0])
		n2 = int(entrada[2])
		result = n1+n2
		dif = result - resp
		if (dif < 0):
			dif = dif * -1
	elif (operador == '-'):
		n1 = int(entrada[0])
		n2 = int(entrada[2])
		result = n1-n2
		dif = result - resp
		if (dif < 0):
			dif = dif * -1
	elif (operador == 'x'):
		n1 = int(entrada[0])
		n2 = int(entrada[2])
		result = n1*n2
		dif = result - resp
		if (dif < 0):
			dif = dif * -1
	errou = "E"
	for j in range(dif):
		errou = errou + "r"
	errou = errou + "ou!"
	print(errou)