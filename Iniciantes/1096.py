i = 1
j = 7
cont = 0
while i <= 9:
	while cont < 3:
		print "I=%d J=%d" % (i, j)
		j = j - 1
		cont = cont + 1
	cont = 0
	j = 7
	i = i + 2