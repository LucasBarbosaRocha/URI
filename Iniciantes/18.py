numTotal = int(raw_input())

print numTotal

cont = 0
# notas de 100
if numTotal >= 100 :
	while numTotal >= 100:
		numTotal = numTotal - 100
		cont = cont + 1
print "%d nota(s) de R$ 100,00" % cont

cont = 0
# notas de 50
if numTotal >= 50 :
	while numTotal >= 50:
		numTotal = numTotal - 50
		cont = cont + 1
print "%d nota(s) de R$ 50,00" % cont

cont = 0
# notas de 20
if numTotal >= 20 :
	while numTotal >= 20:
		numTotal = numTotal - 20
		cont = cont + 1
print "%d nota(s) de R$ 20,00" % cont

cont = 0
# notas de 10
if numTotal >= 10 :
	while numTotal >= 10:
		numTotal = numTotal - 10
		cont = cont + 1
print "%d nota(s) de R$ 10,00" % cont

cont = 0
# notas de 5
if numTotal >= 5 :
	while numTotal >= 5:
		numTotal = numTotal - 5
		cont = cont + 1
print "%d nota(s) de R$ 5,00" % cont

cont = 0
# notas de 2
if numTotal >= 2 :
	while numTotal >= 2:
		numTotal = numTotal - 2
		cont = cont + 1
print "%d nota(s) de R$ 2,00" % cont

cont = 0
# notas de 1
if numTotal >= 1 :
	while numTotal >= 1:
		numTotal = numTotal - 1
		cont = cont + 1
print "%d nota(s) de R$ 1,00" % cont