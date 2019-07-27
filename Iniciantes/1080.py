num = int(raw_input())
cont = 1
i = 2
while i <= 100:
	num2 = int(raw_input())
	if num2 > num:
		num = num2
		cont = i
	i = i + 1
print "%d\n%d" % (num, cont)