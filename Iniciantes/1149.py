entrada = raw_input().split(" ")
n = int(entrada[1])
a = int(entrada[0])

if n <= 0:
	while n <= 0:
		n = int(raw_input())

i = 1
while n > 1:
	a = a + (int(entrada[0])+i)
	i = i + 1
	n = n - 1
print a