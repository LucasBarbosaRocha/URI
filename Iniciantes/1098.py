i = 0
j = 1
cont = 3
print "I=%d J=%d" % (i,j)
print "I=%d J=%d" % (i,j+1)
print "I=%d J=%d" % (i,j+2)	

i = 0.2
while i <= 1.8:
	while cont > 0:
		if i == 1:
			print "I=%d J=%d" % (i,j+i)
		else:
			print "I=%.1f J=%.1f" % (i,j+i)
		j = j + 1
		cont = cont - 1
	cont = 3
	j = 1
	i = i + 0.2


i = 2
j = 1
print "I=%d J=%d" % (i,j+2)
print "I=%d J=%d" % (i,j+3)
print "I=%d J=%d" % (i,j+4)		