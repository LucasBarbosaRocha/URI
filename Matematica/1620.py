while True:
	try:
		L = int(raw_input())	

		if L == 0:
			break

		I = float(L + (L - 3.0))
		x = float((I-L)/L)
		print "%.6f " % x

	except:
		break

