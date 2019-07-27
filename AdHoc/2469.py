notas = [0]*101


n = int(input())
entrada = input().split(" ")

for i in range(n):
	pos = int(entrada[i])
	notas[pos] = notas[pos] + 1

#print (notas)

notaM = 0
nota = 0
for i in range(101):
	if (notas[i] >= notaM):
		notaM = notas[i]
		nota = i
print (nota)