n = int(input())
for i in range(n):
	linguas = int(input())
	lingua = input()
	v = 1
	for j in range(1, linguas):
		lingua2 = input()
		if (lingua != lingua2):
			v = 0

	if (v == 1):
		print (lingua)
	else:
		print ("ingles")