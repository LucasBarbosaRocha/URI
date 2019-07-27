def maior(a,b):
	if a > b:
		return a
	else:
		return b

def menor(a,b):
	if a < b:
		return a
	else:
		return b		

number1 = int(raw_input())
number2 = int(raw_input())

aux = menor(number1,number2)
tmp = maior(number1,number2)

soma = 0
for aux in range(aux, tmp+1):
	if aux % 13 != 0:
		soma = soma + aux

print soma