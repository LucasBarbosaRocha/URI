lista = []
while True:
	try:
		entrada = raw_input()
		tam = len(entrada)
	
		palavra = ""
		letra = ""
		for i in range(tam):
			letra = entrada[i].lower()
			if (letra.isalpha()):
				palavra = palavra + letra
			else:
				if (len(palavra) > 0):
					lista.append(palavra)
					palavra = ""

		if (len(palavra) > 0):
			lista.append(palavra)
	except :	
		break
#lista.sort()
lista = sorted(set(lista))
tam = len(lista)
for i in range(tam):
	print ("%s" %lista[i])