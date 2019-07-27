i = 0
j = 1
cont = 3
while i <= 2:
	while cont > 0:
		if i == 0 or i == 1 or i == 2:
			print "I=%d J=%d" % (i,j+i)
		else:
			print "I=%.1f J=%.1f" % (i,j+i)
		j = j + 1
		cont = cont - 1
	cont = 3
	j = 1
	i = i + 0.2
