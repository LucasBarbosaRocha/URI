par = []
contPar = 0
impar = []
contImpar = 0
for i in range(15):
	num = int(raw_input())

	if num % 2 == 0:
		contPar = contPar + 1
		par.append(num)
		if contPar == 5:
			for i in range(contPar):
				print "par[%d] = %d" % (i, par[i])
			par = []				
			contPar = 0			
	else:
		contImpar = contImpar + 1
		impar.append(num)
		if contImpar == 5:
			for i in range(contImpar):
				print "impar[%d] = %d" % (i, impar[i])
			impar = []
			contImpar = 0
			
if contImpar != 0:
	for i in range(contImpar):
		print "impar[%d] = %d" % (i, impar[i])
if contPar != 0:
	for i in range(contPar):
		print "par[%d] = %d" % (i, par[i])




