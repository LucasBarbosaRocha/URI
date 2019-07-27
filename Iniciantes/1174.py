v = []

n = 100
for i in range(n):
	v.append(raw_input());

for i in range(n):
	if float(v[i]) <= 10.0 :
		print "A[%d] = %.1f" % (i, float(v[i]))