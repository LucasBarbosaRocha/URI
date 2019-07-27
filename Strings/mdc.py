def mdc(a , b):
	dividendo = max(a, b)
	divisor = min(a, b)
	resto = -1
	quociente = 0

	resto = dividendo % divisor

	while (resto != 0):
		dividendo = divisor
		divisor = resto
		resto = dividendo % divisor
	return divisor

a = int(input())
b = int(input())
print (mdc(a,b))