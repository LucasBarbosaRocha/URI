import math

entrada = raw_input().split(" ")
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])
d = int(entrada[3])

limite = int(math.ceil(math.sqrt(float(c))))

achei = -1
for i in xrange(1, limite):
	if c % i == 0:
		if i%a == 0 and i%b != 0 and d%i != 0:
			achei = i
			break

if achei == -1:
	for i in xrange(2, limite):
		if c % i == 0:
			aux = c/i
			if aux%a == 0 and aux%b != 0 and d%aux != 0:
				achei = aux
				break

print achei
