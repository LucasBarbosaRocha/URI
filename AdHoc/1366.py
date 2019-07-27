while True:
	n = int(input())
	if (n == 0):
		break
	else:
		soma = 0
		for i in range(n):
			entrada = input().split(" ")
			c = int(entrada[0])
			v = int(entrada[1])
			soma = soma + (v // 2)
		result = soma // 2
		print (result)
