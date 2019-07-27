i = 1
j = 7
val = 7
while i <= 9:
	print "I=%d J=%d" %(i,j)
	j = j - 1
	if j == (val-3):
		j = val + 2
		val = val + 2
		i = i + 2