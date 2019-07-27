def mdcEuclides(n1, n2):
	resto = n1%n2
	while (resto != 0):
		n1 = n2
		n2 = resto
		resto = n1%n2
	return n2


n1 = int(input())
n2 = int(input())

print ("MDC(%d,%d) = %d" %(n1, n2, mdcEuclides(n1,n2)))