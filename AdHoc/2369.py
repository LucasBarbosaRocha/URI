consumo = int(input())
gasto = 7
if consumo > 10:
    if consumo > 30:
        gasto += 20
    else:
        aux = consumo - 10
        gasto += aux
if consumo > 30:
    if consumo > 100:
        gasto += 140
    else:
        aux = consumo - 30
        gasto += (aux*2)

if consumo > 100:
    aux = consumo - 100
    gasto += (aux*5)
    
print (gasto)