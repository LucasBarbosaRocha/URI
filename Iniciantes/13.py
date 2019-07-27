def major(a, b):
	c = a - b
	if c < 0:
		c = c * (-1)
	return (a+b+(c))/2


#main

a = int(raw_input())
b = int(raw_input())
c = int(raw_input())

maior = major(a, b)
maior = major(maior, c)

print "%d eh o maior" % maior