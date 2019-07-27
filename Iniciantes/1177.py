num = int(raw_input())
cont = 0

i = 0
vector = []
while i < 1000:
	vector.append(cont)
	print "N[%d] = %d" % (i, cont)
	cont = cont + 1
	if cont == num:
		cont = 0
	i = i + 1