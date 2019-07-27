def rafael(a, b):
	return ((3*a)**2) + (b**2)

def beto(a, b):
	return (2*(a**2)) + ((5*b)**2)

def carlos(a, b):
	return ((100*-1)*a) + (b**3)

n = int(input())
for i in range(n):
	entrada = input().split(" ")
	a = int(entrada[0])
	b = int(entrada[1])

	r = rafael(a,b)
	be = beto(a,b)
	c = carlos(a,b)

	#print (r, b, c)
	maior = max(max(r,be),c)

	if (maior == r):
		print ("Rafael ganhou")
	elif (maior == be):
		print ("Beto ganhou")
	else:
		print ("Carlos ganhou")



