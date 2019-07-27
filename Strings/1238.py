def remove(palavra, inicio):
	resto = ""
	for i in range(inicio, len(palavra)):
		resto = resto + palavra[i]
	return resto

casos = int(input())
while casos > 0:
	entrada = raw_input().split(" ")
	p1 = entrada[0]
	p2 = entrada[1]

	tamP1 = len(p1)
	tamP2 = len(p2)

	result = ""
	if tamP1 == tamP2:
		for i in range(tamP1):
			result = result + p1[i]
			result = result + p2[i]		
	elif tamP1 < tamP2:
		for i in range(tamP1):
			result = result + p1[i]
			result = result + p2[i]
		result = result + remove(p2, tamP1)
	else:
		for i in range(tamP2):
			result = result + p1[i]
			result = result + p2[i]
		result = result + remove(p1, tamP2)		

	print result
	casos = casos - 1