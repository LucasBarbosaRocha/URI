def imprime(salario, reajuste, percentual):
	print "Novo salario: %.2f" % salario
	print "Reajuste ganho: %.2f" % reajuste
	print "Em percentual: %d %% " % percentual

salario = float(input())
tmp = 0

if salario <= 400.00 :
	tmp = salario * 0.15
	imprime(salario+tmp,tmp,15)
elif salario > 400.00 and salario <= 800.00 :
	tmp = salario * 0.12
	imprime(salario+tmp,tmp,12)	
elif salario > 800.00 and salario <= 1200.00 :
	tmp = salario * 0.10
	imprime(salario+tmp,tmp,10)	
elif salario > 1200.00 and salario <= 2000.00 :
	tmp = salario * 0.07
	imprime(salario+tmp,tmp,7)	
elif salario > 2000.00 :
	tmp = salario * 0.04
	imprime(salario+tmp,tmp,4)	