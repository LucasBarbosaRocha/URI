while True:
	n = int(input())
	if (n == 0):
		break
	for j in range(n):
		entrada = input()
		tam = len(entrada)
		z = 0
		u = 0

		for i in range(tam):
			if (i % 2 == 0):
				z = z + int(entrada[i])
			else:
				u = u + int(entrada[i])
		#print (z, u)
		z = str(z)
		u = str(u)
		result = 0
		for i in range(len(z)):
			result = result + int(z[i])
		for i in range(len(u)):
			result = result + int(u[i])
		print (result)


