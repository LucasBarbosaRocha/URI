i = 3
j = 2
s = 1
while i <= 39:
	s = s + (i/float(j))
	i = i + 2
	j = j * 2
print "%.2f" % s