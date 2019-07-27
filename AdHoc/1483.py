bicho = [0] * 100
c = 0
k = 1
for i in range(1,100):
	if (c < 4):
		bicho[i] = k
		c = c + 1
	else:
		k = k + 1
		bicho[i] = k
		c = 1


while True:
	entrada = input().split()

	if (entrada[0] == "0" and entrada[1] == "0" and entrada[2] == "0"):
		break

	v = float(entrada[0])


	if (len(entrada[1]) == 1):
		n = "000"+entrada[1]
	elif (len(entrada[1]) == 2):
		n = "00"+entrada[1]
	elif (len(entrada[1]) == 3):
		n = "0"+entrada[1]
	else:
		n = entrada[1]

	if (len(entrada[2]) == 1):
		m = "000"+entrada[2]
	elif (len(entrada[2]) == 2):
		m = "00"+entrada[2]
	elif (len(entrada[2]) == 3):
		m = "0"+entrada[2]
	else:
		m = entrada[2]

	result = 0
	if (len(n) >= 4 and len(m) >= 4):
		auxN = n[len(n) - 4:]
		auxM = m[len(m) - 4:]
		if (auxN == auxM):
			result = v * 3000
	if (len(n) >= 3 and len(m) >= 3):
		auxN = n[len(n) - 3:]
		auxM = m[len(m) - 3:]
		if (auxN == auxM):
			resultAux = v * 500
			if (resultAux >= result):
				result = resultAux
	if (len(n) >= 2 and len(m) >= 2):
		auxN = n[len(n) - 2:]
		auxM = m[len(m) - 2:]
		if (auxN == auxM):
			resultAux = v * 50
			if (resultAux >= result):
				result = resultAux

	if (len(n) >= 2 and len(m) >= 2):
		auxN = int(n[len(n) - 2:])
		auxM = int(m[len(m) - 2:])
		if (bicho[auxM] == bicho[auxN]):
			resultAux = v * 16
			if (resultAux >= result):
				result = resultAux

	print("%.2f" %result)
