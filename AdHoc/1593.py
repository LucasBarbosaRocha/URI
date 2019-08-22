t = int(input())
for i in range(t):
	a = input()
	b = bin(int(a))
	qtd = 0
	for j in range(len(b)):
		if (b[j] == '1'):
			qtd += 1
	print (qtd)