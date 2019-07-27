num = float(raw_input())

i = 1
vector = [num]
print "N[0] = %.4f" % num
while i < 100:
	num = num/2.0
	vector.append(num)
	print "N[%d] = %.4f" % (i, num)
	i = i + 1