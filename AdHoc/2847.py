entrada = input()
I=l=o=v=e=y=u=sim=0
for i in range(len(entrada)):
	if (entrada[i] == 'I'):
		I = I + 1
	if (entrada[i] == 'l'):
		l = l + 1
	if (entrada[i] == 'o'):
		o = o + 1
	if (entrada[i] == 'v'):
		v = v + 1
	if (entrada[i] == 'e'):
		e = e + 1
	if (entrada[i] == 'y'):
		y = y + 1
	if (entrada[i] == 'u'):
		u = u + 1
	if (entrada[i] == '!'):
		sim = sim + 1

qtd = 0
while (I > 0 and l > 0 and o >= 2 and v > 0 and e > 0 and y > 0 and u > 0 and sim > 0):
	qtd = qtd + 1
	I = I - 1
	l = l - 1
	o = o - 2
	v = v - 1
	e = e - 1
	y = y - 1
	u = u - 1
	sim = sim - 1

print(qtd)