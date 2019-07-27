N = int(input())
entrada = input().split(" ")
saida = ""
for i in range(len(entrada)):
	palavra = entrada[i]
	if (len(palavra) == 3):
		if (i < len(entrada) - 1):
			if (palavra[0] == 'O' and palavra[1] == 'B'):
				saida = saida + "OBI "
			elif (palavra[0] == 'U' and palavra[1] == 'R'):
				saida = saida + "URI "
			else:
				saida = saida + palavra + " "
		else:
			if (palavra[0] == 'O' and palavra[1] == 'B'):
				saida = saida + "OBI"
			elif (palavra[0] == 'U' and palavra[1] == 'R'):
				saida = saida + "URI"
			else:
				saida = saida + palavra
	else:
		if (i < len(entrada) - 1):
			saida = saida + palavra + " "
		else:
			saida = saida + palavra			
print(saida)