entrada = raw_input().split(" ")
msg = ""
i = 1
cont = 0
while i <=  int(entrada[1]):
	msg = msg + " " + str(i)
	cont = cont + 1
	if cont == 3:
		print msg
		cont = 0
		msg = ""
	i = i + 1