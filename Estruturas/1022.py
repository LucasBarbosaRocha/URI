def mmc(n1, n2):
	result = 1
	div = 2
	while (n1 > 1 or n2 > 1):
		if (n1 % div == 0 or n2 % div == 0):
			result = result * div
		if (n1 % div == 0):
			n1 = n1 / div
		if (n2 % div == 0):
			n2 = n2 / div
		if (not (n1 % div == 0 or n2 % 2 == 0)):
			div = div + 1
	return result

def mdc(n1, n2):
	result = 1
	div = 2
	#print("MDC")
	while (n1 > 1 or n2 > 1):
		#print (n1, n2)
		if (n1 % div == 0 and n2 % div == 0):
			result = result * div
		if (n1 % div == 0):
			n1 = n1 / div
		if (n2 % div == 0):
			n2 = n2 / div
		if (not (n1 % div == 0 and n2 % 2 == 0)):
			div = div + 1
		if (div > n1 or div > n2):
			break
	#print("----------")
	return result		


n = int(input())

for i in range(n):
	entrada = input()
	entrada = entrada.replace(" ","")
	tam = len(entrada)
	v = 1
	j = 0
	while (entrada[j].isdigit() or entrada[j] == '/'):
		if (entrada[j] == '/'):
			if (v > 1):
				break
			v = v + 1
		j = j + 1

	sinal = entrada[j]
	pos = j
	#print ("sinal %s" %sinal)
	#print (entrada, sinal)
	parte1 = entrada[:pos]
	parte2 = entrada[pos+1:]
	#print(parte1, sinal, parte2)
	j = 0
	while (parte1[j].isdigit()):
		j = j + 1
	n1 = int(parte1[:j])
	d1 = int(parte1[j+1:])
	j = 0
	while (parte2[j].isdigit()):
		j = j + 1	
	n2 = int(parte2[:j])
	d2 = int(parte2[j+1:])

	#print (n1,d1,n2,d2)

	if (sinal == '+'):
		numerador = (n1*d2)+(n2*d1)
		denominador = (d1*d2)
		m = mmc(d1, d2)
		numeradorSimpl = ((m/d1) * n1) + ((m/d2) * n2)
		m2 = mdc(numeradorSimpl, m)
		#print(numeradorSimpl, m, m2)
		numeradorSimpl = numeradorSimpl/m2
		denominadorSimpl = m/m2
		print("%d/%d = %d/%d" %(numerador, denominador, numeradorSimpl, denominadorSimpl))
	elif (sinal == '-'):
		numerador = (n1*d2)-(n2*d1)
		denominador = (d1*d2)
		m = mmc(d1, d2)
		numeradorSimpl = ((m/d1) * n1) - ((m/d2) * n2)
		m2 = mdc(numeradorSimpl, m)
		#print(numeradorSimpl, m, m2)
		numeradorSimpl = numeradorSimpl/m2
		denominadorSimpl = m/m2
		print("%d/%d = %d/%d" %(numerador, denominador, numeradorSimpl, denominadorSimpl))
	elif (sinal == '*'):
		numerador = n1*n2
		denominador = d1*d2
		m = mdc(numerador, denominador)
		numeradorSimpl = numerador/m
		denominadorSimpl = denominador/m
		print("%d/%d = %d/%d" %(numerador, denominador, numeradorSimpl, denominadorSimpl))
	elif (sinal == '/'):
		numerador = n1*d2
		denominador = n2*d1
		m = mdc(numerador, denominador)
		numeradorSimpl = numerador/m
		denominadorSimpl = denominador/m
		print("%d/%d = %d/%d" %(numerador, denominador, numeradorSimpl, denominadorSimpl))
