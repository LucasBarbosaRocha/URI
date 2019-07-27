casos = int(raw_input())
i = 0
while i < casos: # vamos percorrer i vezes representando os casos de entrada
	entrada = raw_input().split(" ")
	n1 = float(entrada[0]) * 2
	n2 = float(entrada[1]) * 3
	n3 = float(entrada[2]) * 5
	media = (n1+n2+n3)/10
	print "%.1f" % media
	i = i + 1 