from operator import itemgetter

n = int(input())
while n > 0:
	entrada = input()
	tam = len(entrada)
	entrada = entrada.lower()
	recorrentes = {
		"a": 0, "b": 0,"c": 0, "d": 0,"e": 0, "f": 0,
		"g": 0, "h": 0,"i": 0, "j": 0,"k": 0, "l": 0,
		"m": 0, "n": 0,"o": 0, "p": 0,"q": 0, "r": 0,
		"r": 0, "s": 0,"t": 0, "u": 0,"v": 0, "w": 0,
		"x": 0, "y": 0,"z": 0
	}

	for i in range(tam):
		if entrada[i] >= 'a' and entrada[i] <= 'z':
			letra = entrada[i]
			recorrentes[letra] = recorrentes[letra] + 1
	v = 0
	r = 0
	letra = ""
	#print(recorrentes)
	#for i in recorrentes.values():
	for i in recorrentes:
		if (v == 0):
			value = recorrentes[i]
			v = 1
		else:
			#print("value %d r %d" %(recorrentes[i], value))
			if (recorrentes[i] != 0 and recorrentes[i] == value):
				r = r + 1
			elif (recorrentes[i] != 0 and recorrentes[i] > value):
				value = recorrentes[i]
				r = 0
				letra = i

	#print("value %d r %d" %(value, r))
	#if (r > 0):
	result = ""
	for i in recorrentes:
		if (recorrentes[i] == value):
			result = result + i
	result = sorted(result)
	resultOficial = ""
	for i in result:
		resultOficial = resultOficial + i
	print(resultOficial)	
	#else:
		#print(letra)

	n = n -1