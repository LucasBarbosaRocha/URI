cont = 0
soma = 0.0
i = 0
while i < 6:
	num = float(raw_input())
	if num > 0:
		soma = soma + num
		cont = cont + 1
	i = i + 1
print "%d valores positivos\n%.1f" % (cont, soma/float(cont))