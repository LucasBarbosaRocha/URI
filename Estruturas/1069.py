n = int(input())
for i in range(n):
	entrada = input()
	tam = len(entrada)
	diamantes = 0
	abertos = 0
	fechados = 0
	t1 = 0
	t2 = 0
	lista = ""
	for j in range(tam):
		#<..><.<..>>
		if (entrada[j] == '<'):
			lista = lista + '<'
		if (entrada[j] == '>'):
			lista = lista + '>'	
	#print (lista)
	tam2 = len(lista)
	abertos = []
	for j in range(tam2):
		if (lista[j] == '<'):
			abertos.append('<')
			t1 = t1 + 1
		if (lista[j] == '>'):
			if (len(abertos) > 0):
				t2 = t2 + 1
				abertos.remove('<')
	print (t2)	