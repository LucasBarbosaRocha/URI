n = int(input())
for i in range(n):
	entrada = input().split(" ")
	a = entrada[0]
	b = entrada[1]

	if (len(a) < len(b)):
		print ("nao encaixa")
	else:
		tamB = len(b)
		aux = a[len(a)-tamB:len(a)]
		if (b == aux):
			print ("encaixa")
		else :
			print ("nao encaixa")