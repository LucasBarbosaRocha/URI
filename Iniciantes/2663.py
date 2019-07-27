n = input()
p = input()
l = []

for i in range(n):
	aux = input()
	l.append(aux)

l.sort()

tam = len(l)

tam = tam - p
value = l[tam]
tam = tam - 1
cont = p

while tam >= 0 and value == l[tam]:
	cont = cont + 1
	tam = tam - 1

print cont
