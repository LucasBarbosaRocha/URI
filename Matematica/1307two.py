test = int(raw_input())

for k in range(1,test+1):
	s1 = raw_input()
	s2 = raw_input()


	#binaryToDecimal
	tam = len(s1)
	elevar = tam-1
	soma = 0

	for i in range(tam):
		if s1[i] == '1':
			soma = soma + (2**elevar)
		elevar = elevar - 1	
	s1Decimal = soma

	#binaryToDecimal
	tam = len(s2)
	elevar = tam-1
	soma = 0

	for i in range(tam):
		if s2[i] == '1':
			soma = soma + (2**elevar)
		elevar = elevar - 1	
	s2Decimal = soma

	#maior e menor
	if s1Decimal > s2Decimal:
		maior = s1Decimal
		menor = s2Decimal
	else:
		maior = s2Decimal
		menor = s1Decimal

	#mdc de euclides
	dividendo = maior
	divisor = menor
	resto = dividendo % divisor

	while resto != 0:
		resto = dividendo%divisor
		dividendo = divisor
		if resto == 0:
			break
		divisor = resto

	mdc = divisor

	if mdc > 1:
		print "Pair #%d: All you need is love!" % k
	else:
		print "Pair #%d: Love is not all you need!" % k

