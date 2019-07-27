while True:
	entrada = raw_input().split(" ")
	ini = int(entrada[0])
	fim = int(entrada[1])
	vector = [0,0,0,0,0,0,0,0,0,0] 
	resto = 0

	if ini == 0 and fim == 0:
		break

	while ini <= fim:

		tmp = ini

		while True:
			resto = tmp % 10
			aux = vector[resto]
			vector[resto] = aux + 1
			tmp = tmp / 10
			if tmp == 0:
				break

		ini = ini + 1

	msg = str(vector[0])
	i = 1
	while i < 10:
		msg = msg + " " + str(vector[i])
		i = i + 1

	print msg
