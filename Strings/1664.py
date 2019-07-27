def mdc(a , b):
	dividendo = max(a, b)
	divisor = min(a, b)
	resto = -1
	quociente = 0

	resto = dividendo % divisor

	while (resto != 0):
		dividendo = divisor
		divisor = resto
		resto = dividendo % divisor
	return divisor

entrada = ""
palavras = 0
bullshit = 0
validas = []
somaAux = 0

while True:
	try:
		entrada = input()
		entrada = entrada.lower()
		entrada = entrada.split(" ")
		tam = len(entrada)

		#print (entrada)
		for i in range(tam):
			palavra = entrada[i]
			#print (palavra)
			if (palavra.isalpha() and palavra not in validas and palavra != "bullshit"):
				#print ("palavra valida %s" %palavra)
				validas.append(palavra)
				palavras = palavras + 1
			elif (palavra.isalpha() and palavra == "bullshit"):
				validas = []
				bullshit = bullshit + 1
				somaAux = somaAux + palavras
				palavras = 0
				#print("------------")
			elif (not palavra.isalpha()):
				tmp = entrada[i]
				tam2 = len(tmp)
				j = 0
				while (j < tam2):
					aux = ""
					while (j < tam2 and tmp[j].isalpha()):
						#print (tmp[j])
						aux = aux + tmp[j]
						j = j + 1
					if (aux != "" and aux not in validas):
						validas.append(aux)
						#print ("2 - palavra valida %s original %s" %(aux, tmp))
						palavras = palavras + 1
					j = j + 1
	except :
		break

#print ("Antes")
#print (somaAux, bullshit)
div = mdc(somaAux, bullshit)
print ("%d / %d" %((somaAux/div), (bullshit/div)))