def converte(n):
	aux = n
	while (len(n) > 1):
		i = 0
		tmp = 0
		while (i < len(n)):
			tmp = tmp + int(n[i])
			i = i + 1
		#print (tmp)
		n = str(tmp)
	return int(n)


while True:
	entrada = input().split(" ")
	n = int(entrada[0])
	m = int(entrada[1])

	if (n == 0 and m == 0):
		break

	auxN = converte(str(n))
	auxM = converte(str(m))

	if (auxN > auxM):
		print("1")
	elif (auxN < auxM):
		print("2")
	else:
		print("0")

