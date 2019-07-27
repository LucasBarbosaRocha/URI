while True:
	n = int(input())
	if (n == 0):
		break
	lista = []
	dic = {}
	qtdLetras = 0
	barraN = 0
	for i in range(n):
		entrada = input()
		tam = len(entrada)
		qtdLetras = qtdLetras + tam
		if (barraN > 0):
			entrada = sobra + entrada
		barraN = barraN + 1
		j = 0
		while (j < tam - 1):
			#lista.append(entrada[j:j+2])
			digrafo = entrada[j:j+2]
			if (digrafo not in dic):
				dic[digrafo] = 1
			else:
				dic[digrafo] = dic[digrafo] + 1				
			j = j + 1
		sobra = entrada[len(entrada)-1:len(entrada)]
		#print ("Sobra %s" %sobra)
	qtdLetras = qtdLetras - (barraN - 1)
	print(dic)
	b = [(k, dic[k]) for k in sorted(dic, key=dic.get, reverse=True)]
	print ("-------------")
	print(b)
	print(qtdLetras)

	for i in range(5):
		palavra = b[i]
		dig = palavra[0]
		frequencia = int(palavra[1])
		print ("%s %s %.6f" %(dig, frequencia, (frequencia / qtdLetras)))