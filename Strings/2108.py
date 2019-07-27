maior = ""
tamMaior = 0
aux = 1
while True:
	entrada = input().split(" ")
	if (entrada[0] == '0'):
		break
	resposta = ""
	for i in range(len(entrada)):
		palavra = entrada[i]
		n = len(palavra)
		if (aux == 1):
			maior = palavra
			tamMaior = n
			aux = 0
		elif (n >= tamMaior):
			tamMaior = n
			maior = palavra

		if (i < len(entrada) - 1):
			resposta = resposta + str(n) + "-"
		else:
			resposta = resposta + str(n)
	print (resposta)
print()
print("The biggest word: %s" %maior)
