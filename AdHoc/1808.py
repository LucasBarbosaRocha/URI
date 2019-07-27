entrada = input()
num = 0
qtd = 0
i = 0
while i < len(entrada):
	j = i
	aux = entrada[j]
	j = j + 1
	while j < len(entrada) and entrada[j] == '0':
		aux = aux + entrada[j]
		j = j + 1
	i = j
	qtd = qtd + 1
	num = num + int(aux)
	#print(aux, num, qtd)
print ("%.2f" %(num/qtd))
