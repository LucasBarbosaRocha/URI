number = int(raw_input())

cont = 1
for i in range(number):
	msg = ""
	for j in range(cont, cont+3):
		msg = msg + str(j) + " "
	msg = msg + str("PUM")
	print msg
	cont = cont+4