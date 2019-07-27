n = int(input())
for i in range(n):
	entrada = input().split(" ")
	pesos = input().split(" ")
	pesoMax = int(entrada[1])
	somaPesos = 0
	qtd = 0
	for j in range(len(pesos)):
		p = int(pesos[j])
		if (somaPesos + p <= pesoMax):
			somaPesos = somaPesos + p
		else:
			somaPesos = p
			qtd = qtd + 1
	if (somaPesos <= pesoMax):
		qtd = qtd + 1
	print(qtd)