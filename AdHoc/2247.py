n = 1
while True:
	N = int(input())
	if (N == 0):
		break
	print("Teste %d" %n)
	n = n + 1
	cj = 0
	cz = 0
	for i in range(N):
		entrada = input().split(" ")
		j = int(entrada[0])
		z = int(entrada[1])
		cj = cj + j
		cz = cz + z
		print(cj-cz)
		menor = min(j,z)
		cj = cj - menor
		cz = cz - menor
	print()