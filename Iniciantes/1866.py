casos = int(raw_input())

while casos > 0:
	num = int(raw_input())
	# S = 1-1+1-1+1-1+1 ...

	if num % 2 == 0:
		print "0"
	else:
		print "1"
	casos = casos - 1

