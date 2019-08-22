while True:
	n = int(input())
	if (n == 0):
		break
	entrada = input().split(" ")
	for i in range(len(entrada)):
		entrada[i] = int(entrada[i])
	value = sorted(entrada)[-2]
	index = entrada.index(value)
	print(index + 1)