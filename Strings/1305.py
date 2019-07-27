while True:

	try:
		num = input().split(".")
		cutoff = float(input())
		#print (num, cutoff)
		if (num[0] != ''):
			numOficial = int(num[0])
		else:
			numOficial = 0
		quebrado   = 0
		#print("Teste %d" %numOficial)

		if (len(num) > 1):
			quebrado = "0." + num[1]
			quebrado = float(quebrado)

		#print("Quebrado %f %f" %(quebrado, cutoff))

		if (quebrado > cutoff):
			numOficial =  numOficial + 1
		print(numOficial)
	except :
		break