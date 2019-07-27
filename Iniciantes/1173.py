num = int(raw_input())

vector = [num]

for i in range(10):
	num = num * 2
	vector.append(num)
	print "N[%d] = %d" % (i, vector[i])
