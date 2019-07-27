n = int(input())
for i in range(n):
	entrada = input().split(" ")
	qtd = int(entrada[0])
	pos = int(qtd / 2) + 1
	print("Case %d: %s" %((i+1),entrada[pos]))