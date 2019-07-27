n = int(input())
for i in range(n):
	entrada = input().split(" ")
	tam = len(entrada)

	for j in range(1, tam):
		firstWord = entrada[j]
		tamAux = len(firstWord)
		l = j - 1
		while (l >= 0 and len(entrada[l]) < tamAux):
			entrada[l + 1] = entrada[l]
			l = l - 1
		entrada[l + 1] = firstWord

	resposta = ""
	for j in range(tam):
		if (j < tam - 1):
			resposta = resposta + entrada[j] + " "
		else:
			resposta = resposta + entrada[j]

	print(resposta)