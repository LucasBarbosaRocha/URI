n = input()

for i in range(n):
	entrada = raw_input()
	j = 1
	cont = 0
	while entrada[j] == 'a':
		cont = cont + 1
		j = j + 1
	j = j + 3
	cont2 = 0
	while entrada[j] == 'a':
		cont2 = cont2 + 1
		j = j + 1

	str = 'k'
	for j in range(cont*cont2):
		str = str + 'a'

	print str