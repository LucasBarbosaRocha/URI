n = int(raw_input())

while n > 0:
	v = [0,1,1]
	pos = int(raw_input())

	if pos > 2 :
		i = 3
		while i <= pos :
			v.append(v[i-1]+v[i-2])
			i = i + 1


	print "Fib(%d) = %d" % (pos, v[pos])

	n = n - 1