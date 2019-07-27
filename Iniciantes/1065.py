cont = 0
while True:
	try:
		num = int(raw_input())
		if num % 2 == 0:
			cont = cont + 1
	except:
		break

print "%d valores pares" % cont