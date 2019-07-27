def maior(n1, n2):
	if n1 > n2:
		return n1
	else:
		return n2

def menor(n1,n2):
	if n1 < n2:
		return n1
	else:
		return n2

def euclides(n1, n2):
	dividendo = maior(n1,n2)
	divisor = menor(n1,n2)
	resto = dividendo % divisor

	while resto != 0:
		resto = dividendo%divisor
		dividendo = divisor
		if resto == 0:
			return divisor
		divisor = resto
	return divisor

def binaryToDecimal(number):

	tam = len(number)
	elevar = tam-1
	soma = 0

	for i in range(tam):
		if number[i] == '1':
			soma = soma + (2**elevar)
		elevar = elevar - 1
	return soma

test = int(raw_input())

for i in range(1,test+1):
	s1 = raw_input()
	s2 = raw_input()


	s1Decimal = binaryToDecimal(s1)
	s2Decimal = binaryToDecimal(s2)
	mdc = euclides(s1Decimal,s2Decimal)

	if mdc > 1:
		print "Pair #%d: All you need is love!" % i
	else:
		print "Pair #%d: Love is not all you need!" % i

