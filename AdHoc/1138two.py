while True:
	entrada = raw_input().split(" ")
	ini = int(entrada[0])
	fim = int(entrada[1])
	p = [1,0,0,0,0,0,0,0,0,0]
	num = [1,0,0,0,0,0,0,0,0,0]
	v = [0,0,0,0,0,0,0,0,0,0]

	if ini == 0 and fim == 0:
		break

	i = 1
	while i < 10:
		p[i] = 10 * p[i-1]
		i = i + 1
	i = 1
	while i < 10:
		num[i] = 9 * num[i-1]
		i = i + 1

	for i in range(10):
		print "%d " % p[i]

	for i in range(10):
		print "%d " % num[i]	