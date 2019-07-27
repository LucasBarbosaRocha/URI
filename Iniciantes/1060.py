cont = 0
i = 0

while i < 6:
	num = float(raw_input())
	if num > 0:
		cont = cont + 1
	i = i + 1

print "%d valores positivos" % cont