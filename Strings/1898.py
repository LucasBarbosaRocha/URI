linha1 = raw_input()
linha2 = raw_input()
tam1 = len(linha1)
tam2 = len(linha2)
cpf = ""
valor1 = ""
valor2 = ""

i = 0
j = 0
while i < 11 and j < tam1:
	if (linha1[j].isdigit()):
		cpf = cpf + linha1[j]
		i = i + 1
	j = j + 1
p = 0
while j < tam1:

	if (p == 0 and linha1[j].isdigit()):
		valor1 = valor1 + linha1[j]
	elif (linha1[j] == '.'):
		if (p > 0):
			break		
		valor1 = valor1 + "."
		p = p + 1
	elif (p < 3 and linha1[j].isdigit()):
		valor1 = valor1 + linha1[j]
		p = p + 1
	j = j + 1

j = 0
p = 0
while j < tam2:

	if (p == 0 and linha2[j].isdigit()):
		valor2 = valor2 + linha2[j]
	elif (linha2[j] == '.'):
		if (p > 0):
			break
		valor2 = valor2 + "."
		p = p + 1
	elif (p < 3 and linha2[j].isdigit()):
		valor2 = valor2 + linha2[j]
		p = p + 1
	j = j + 1

print ("cpf %s" %cpf)
#print ("%s" %valor1)
#print ("%s" %valor2)
resultado = float(valor1) + float(valor2)
print ("%.2f" %resultado)