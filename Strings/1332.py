test = int(raw_input())
while test > 0:
	word = raw_input()
	

	if (word[0] == 'o' and word[1] == 'n') or (word[0] == 'o' and word[2] == 'e') or (word[1] == 'n' and word[2] == 'e'):
		print "1" 
	elif (word[0] == 't' and word[1] == 'w') or (word[0] == 't' and word[2] == 'o') or (word[1] == 'w' and word[2] == 'o'):
		print "2"
	else:
		print "3"
	test = test - 1