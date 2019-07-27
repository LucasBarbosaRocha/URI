n = int(input())
for i in range(n):
	entrada = input().split(" ")
	b = int(entrada[0])
	e = int(entrada[1])
	comeco = ""
	fim = ""
	for j in range(b, e+1):
		comeco = comeco + str(j)
	fim = comeco[::-1]
	print ("%s%s" %(comeco,fim))