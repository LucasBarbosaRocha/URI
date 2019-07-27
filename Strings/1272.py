n = int(input())
for i in range(n):
	entrada  = input()
	tam 	 = len(entrada)
	j        = 0
	resposta = ""
	while j < tam:
		if (entrada[j].isalpha()):
			resposta = resposta + entrada[j]
		while (j < tam and entrada[j] != ' '):
			j = j + 1
		j = j + 1
	print (resposta)