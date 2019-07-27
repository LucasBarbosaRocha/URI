v = 0
while True:
	n = int(input())
	if (n == 0):
		break
	elif (v == 1):
		print()
	pessoas = []
	for i in range(n):
		pessoa = input()
		pessoas.append(pessoa)
		if (i == 0):
			tam = len(pessoa)
		else:
			if (len(pessoa) > tam):
				tam = len(pessoa)
	for i in range(n):
		print(pessoas[i].rjust(tam))
	v = 1