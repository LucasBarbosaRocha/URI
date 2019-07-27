while True:
	try:
		n = raw_input()
		nova = ""
		tam = len(n)

		for i in range(tam):
			if n[i] == 'O' or n[i] == 'o':
				nova = nova + '0'
			elif n[i] == 'l':
				nova = nova + '1'
			elif n[i] == ',':
				nova = nova
			elif n[i] == ' ':
				nova = nova
			else:
				nova = nova + n[i]
			
		test = nova.isdigit()

		if test == True:
			number = int(nova)
			if number <= 2147483647:
				print number
			else:
				print "error"
		else:
			print "error"
	except:
		break