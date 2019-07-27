number = int(raw_input())
while number > 0:
	num = raw_input()

	i = 0
	cont = 0

	for i in range(len(num)):
		if num[i] == '0':
			cont = cont + 6
		elif num[i] == '1':
			cont = cont + 2
		elif num[i] == '2':
			cont = cont + 5
		elif num[i] == '3':
			cont = cont + 5
		elif num[i] == '4':
			cont = cont + 4
		elif num[i] == '5':
			cont = cont + 5
		elif num[i] == '6':
			cont = cont + 6
		elif num[i] == '7':
			cont = cont + 3
		elif num[i] == '8':
			cont = cont + 7
		elif num[i] == '9':
			cont = cont + 6

	print "%d leds" % cont
	number = number - 1