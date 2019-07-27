n = int(raw_input())

i = 0
while i < n: 
	entrada = input()

	if entrada % 4 == 0:
		print "1"
	elif entrada % 4 == 1:
		print "7"
	elif entrada % 4 == 2:
		print "9"
	elif entrada % 4 == 3:
		print "3"

	i = i + 1