n = int(input())

while n > 0:
	frase1 = input()
	frase2 = input()
	tam1 = len(frase1)
	tam2 = len(frase2)

	#print (frase1, frase2)
	i = 0
	j = 0
	resposta = ""
	while (i < tam1 and j < tam2):
		k = 0
		while (k < 2):
			resposta = resposta + frase1[i]
			i = i + 1
			k = k + 1
		k = 0
		if (i < tam2):
			while (k < 2):
				resposta = resposta + frase2[j]
				j = j + 1
				k = k + 1
		else :
			resposta = resposta + frase2[tam2 - 1]
	print (resposta)
	n = n - 1