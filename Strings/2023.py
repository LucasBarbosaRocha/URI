lista = []
l = ""
while True:
	try:
		entrada = input()
		l = l + entrada + "+"
	except :
		break
#print (l)
l = l[:len(l) - 1]
original = l.split("+")
lista = l.lower()
lista = lista.split("+")
lista.sort()
escolhido = lista[len(lista) - 1]
for i in range(len(original)):
	if (escolhido == original[i].lower()):
		print (original[i])
		break
