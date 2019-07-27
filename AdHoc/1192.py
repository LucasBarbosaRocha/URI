n = int(input())
for i in range(n):
	entrada = input()
	n1 = int(entrada[0])
	letra = entrada[1]
	n2 = int(entrada[2])

	if (n1 == n2):
		print(n1*n2)
	elif (letra == letra.upper()): # maiusculo
		print(n2-n1)
	else:
		print(n2+n1)
