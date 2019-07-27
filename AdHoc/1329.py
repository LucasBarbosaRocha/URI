while True:
	n = int(input())
	if (n == 0):
		break
	else:
		entrada = input().split(" ")
		mary = entrada.count("0")
		john = entrada.count("1")
		print ("Mary won %d times and John won %d times" %(mary, john))
