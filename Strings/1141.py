import string
# define a funcao a ser usada na comparacao
def comparar(x, y):
  if len(x) > len(y):
    return 1
  elif len(x) == len(y):
    return 0
  else:
    return -1
    
while True:

	n = number = int(raw_input())

	if number == 0:
		break

	lista = []
	while n > 0:
		lista.append(raw_input())
		n = n - 1

	#Ordenar por tamanho de String
	lista.sort(comparar)

	n = number
	result = []
	iAux = n-1
	cont = 0
	pos = 0
	palavra = ""
	i = n - 2
	
	if n == 1:
		print "1"
	else:
		while iAux >= 0:
			compara = string.find(lista[iAux],lista[i])
			if compara >= 0:
				cont = cont + 1
				iAux = i
				palavra = lista[i]


			if i == 0:
				result.append(cont+1)
				if i == 0 and palavra == "":
					break
				cont = 0
				lista.remove(palavra)
				palavra = ""
				n = n - 1
				iAux = n - 1
				i = n - 1

			i = i - 1
		result.sort(reverse=True)
		print result[0]