while True:
	entrada = input().split(" ")
	if (len(entrada) == 1 and entrada[0] == '*'):
		break
	
	tam = len(entrada)
	palavra = entrada[0]
	palavra = palavra.lower()
	i = 1
	v = 1
	while (i < tam):
		palavra2 = entrada[i]
		palavra2 = palavra2.lower()
		if (palavra[0] != palavra2[0]):
			v = 0
			break
		else:
			palavra = palavra2
		i = i + 1
	if (v == 1):
		print("Y")
	else:
		print("N")