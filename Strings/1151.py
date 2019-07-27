n = int(input())
for i in range(n):

	alfabeto = {
		'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0,
		'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
		'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
		's': 0, 't': 0, 'u': 0, 'v': 0, 'x': 0 ,'w': 0,
		'y': 0, 'z': 0
	}

	entrada = input()
	tam = len(entrada)

	for j in range(tam):
		if (entrada[j] != ' ' and entrada[j] != ','):
			alfabeto[entrada[j]] = alfabeto[entrada[j]] + 1
	#print (alfabeto)
	qtd = 0
	letra = ord('a')
	for j in range(len(alfabeto)):
		if (alfabeto[chr(letra)] > 0):
			qtd = qtd + 1
		letra = letra + 1
	#print (qtd)
	if (qtd == 26):
		print("frase completa")
	elif (qtd >= 13 and qtd < 26):
		print("frase quase completa")
	else:
		print("frase mal elaborada")