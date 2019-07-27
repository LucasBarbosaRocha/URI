# -*_ conding: utf-8 _*_

while (1):
	entrada = raw_input().split(" ")

	a = int(entrada[0])
	b = int(entrada[1])

	if (a == 0 and b == 0):
		break	

	aux = b - a
	aux2 = a - aux

	print(aux2)

