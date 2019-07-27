entrada = raw_input().split(" ")

if float(entrada[0]) > 0.0 and float(entrada[1]) > 0.0:
	print "Q1"
elif float(entrada[0]) < 0.0 and float(entrada[1]) > 0.0:
	print "Q2"
elif float(entrada[0]) < 0.0 and float(entrada[1]) < 0.0:
	print "Q3"
elif float(entrada[0]) > 0.0 and float(entrada[1]) < 0.0:
	print "Q4"
elif float(entrada[0]) == 0.0 and float(entrada[1]) == 0.0:
	print "Origem"
elif float(entrada[0]) == 0.0 and float(entrada[1]) != 0.0:
	print "Eixo Y"
elif float(entrada[0]) != 0.0 and float(entrada[1]) == 0.0:
	print "Eixo X"