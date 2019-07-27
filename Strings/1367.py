while True:
	n = int(input())
	if (n == 0):
		break
	s = p = 0
	problemAnterior = []
	incorretos = []
	for i in range(n):
		entrada = input().split(" ")
		problem = entrada[0]
		tempo   = int(entrada[1])
		result  = entrada[2]

		if (result == 'correct'):
			if (i == 0):
				problemAnterior.append(problem)
				p = p + tempo
				s = s + 1
			else:
				if (problem not in problemAnterior):
					s = s + 1
					problemAnterior.append(problem)
					p = p + tempo
		else:
			incorretos.append(problem)

	#print(problemAnterior, incorretos)
	for i in range(len(incorretos)):
		if (incorretos[i] in problemAnterior):
			p = p + 20
	print(s, p)