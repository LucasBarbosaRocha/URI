import sys
n = int(raw_input())
i = 0
menor = sys.maxint
pos = 0
entrada = raw_input().split(" ")
while i < n:
	value = int(entrada[i])
	if value < menor:
		menor = value
		pos = i
	i = i + 1

print "Menor valor: %d" % menor
print "Posicao: %d" % pos