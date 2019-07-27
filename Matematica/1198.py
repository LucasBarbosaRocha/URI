while True:
	try:
		entrada = input().split(" ")
		a = int(entrada[0])
		b = int(entrada[1])
		print ("%d" %abs(a-b))
	except :
		break