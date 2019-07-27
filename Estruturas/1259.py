pares = []
impares  = []
qtd = int(input())
for i in range(qtd):
	n = int(input())
	if (n % 2 == 0):
		pares.append(n)
	else:
		impares.append(n)

pares = sorted(pares)
impares = sorted(impares, reverse=True)
for i in range(len(pares)):
	print(pares[i])
for i in range(len(impares)):
	print(impares[i])