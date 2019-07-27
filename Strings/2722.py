import math
n = int(input())
for i in range(n):
	entrada1 = input()
	entrada2 = input()
	nome = ""
	j = k = 0
	val = 0
	while j < len(entrada1) and k < len(entrada2):
		nome = nome + entrada1[j]
		j = j + 1
		if (j < len(entrada1)):
			nome = nome + entrada1[j]
			j = j + 1
		nome = nome + entrada2[k]
		k = k + 1
		if (k < len(entrada2)):
			nome = nome + entrada2[k]
			k = k + 1
	print(nome)