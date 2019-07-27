import math
v = [4]
for i in range(5, 20000):
	aux = 1
	if math.sqrt(i) % 1 == 0:
		for j in range(len(v)):
			if i % v[j] == 0:
				aux = 0
		if aux == 1:
			v.append(i)
print v