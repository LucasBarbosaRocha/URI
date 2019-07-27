primos = [2, 3, 5, 7]
for i in range(8, 3502):
	if (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0):
		primos.append(i)
print (primos)