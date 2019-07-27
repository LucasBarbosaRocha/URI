qtdTotal = int(raw_input())

# ano
cont = 0
if qtdTotal >= 365:
	while qtdTotal >= 365:
		qtdTotal = qtdTotal - 365
		cont = cont + 1
print "%d ano(s)" % cont

# mes
cont = 0
if qtdTotal >= 30:
	while qtdTotal >= 30:
		qtdTotal = qtdTotal - 30
		cont = cont + 1
print "%d mes(es)" % cont

#dias
cont = 0
if qtdTotal > 0:
	while qtdTotal > 0:
		qtdTotal = qtdTotal - 1
		cont = cont + 1
print "%d dia(s)" % cont