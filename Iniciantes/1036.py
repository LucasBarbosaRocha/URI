import math
entrada = raw_input().split(" ")
a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])

delta = (b*b) - (4*a*c)

if delta < 0.0:
	print "Impossivel calcular"
else:
	if a == 0.0:
		print "Impossivel calcular"
	else:
		raiz = math.sqrt(delta)
		R1 = (((-1)*b)+raiz)/(2*a)
		R2 = (((-1)*b)-raiz)/(2*a)
		print "R1 = %.5f" % R1
		print "R2 = %.5f" % R2
