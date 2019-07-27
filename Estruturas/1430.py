notas = {
	'W': 1, 'H': 1/2, 'Q': 1/4, 'E': 1/8, 'S': 1/16, 'T': 1/32, 'X': 1/64
}

#print (notas)

while True:
	entrada = input()
	if (entrada == '*'):
		break
	else:
		entrada = entrada.split("/")
		tam = len(entrada)
		entrada = entrada[1:tam-1]
		tam = len(entrada)
		#print(entrada)

		qtdCompassos = 0
		for i in range(tam):
			tempo = 0
			for j in entrada[i]:
				tempo = tempo + notas[j]
			if (tempo == 1):
				qtdCompassos = qtdCompassos + 1
		print (qtdCompassos)