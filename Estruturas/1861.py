lista = {}
assasinados = []
while True:
	try :
		entrada = input().split(" ")
		assassino = entrada[0]
		assasinados.append(entrada[1])
		if (assassino in lista):
			lista[assassino] = lista[assassino] + 1
		else :
			lista[assassino] = 1
	except :
		break

tam = len(assasinados)
for i in range(tam):
	if (assasinados[i] in lista):
		del lista[assasinados[i]]
print ("HALL OF MURDERERS")
l = []
for i in lista:
	v = i, lista[i]
	l.append(v)
	#print("%s %d" %(i, lista[i]))
l = sorted(l)
for i in l:
	print("%s %s" %(i[0], i[1]))
