n = int(input())

for i in range(n):
	entrada = input()
	tam = len(entrada)
	soma = 0
	j = 0
	while (j < tam):
		k = j
		number = ""
		while (k < tam and entrada[k].isdigit()):
			number = number + entrada[k]
			k = k + 1
		j = k
		j = j + 1
		if (number != ""):
			#print(number)
			number = int(number)
			soma = soma + number
	print(soma)