while True:
	try:
		N = int(input())
		numeros = []
		for i in range(N):
			entrada = input()
			numeros.append(entrada)
		numeros.sort()
		for i in range(N):
			print("%s" %numeros[i])
	except :
		break