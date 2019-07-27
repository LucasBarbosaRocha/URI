import math

test = int(raw_input())
while test > 0:
	soldados = int(raw_input())
	
	# S = (n(n+1))/2
	# a = n^2; b = n; c = -2*S
	a = 1
	b = 1
	c = (2*soldados)*(-1)

	delta = (b**2) - (4*a*c)
	raiz = math.sqrt(delta)
	n = (((-1)*b) + raiz)/(2*a)
	print int(n)
	test = test - 1