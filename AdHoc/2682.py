r = 0
v = 1
while True:
	try:
		num = int(input())

		if(r <= num and v == 1):
			r = num

		else:
			v = 0

	except :
		break

print(r + 1)