while True:
	try:
		entrada = input().split(" ")
		a = int(entrada[0])
		b = int(entrada[1])

		binA  = bin(a)
		binB  = bin(b)
		strA  = str(binA)
		strB  = str(binB)
		strA  = strA[2:]
		strB  = strB[2:]
		tamA  = len(strA)
		tamB  = len(strB)
		menor = min(tamB,tamA)
		maior = max(tamB,tamA)
		dif   = abs(tamB - tamA)
		resp  = ""

		if (maior == tamA):
			i = maior - 1
			j = tamB - 1
		else:
			i = tamA - 1
			j = maior - 1

		while (i >= dif or j >= dif):
			if (strA[i] == strB[j]):
				resp = "0" + resp
			else:
				resp = "1" + resp
			i -= 1
			j -= 1

		if (dif > 0):
			if (maior == tamA):
				for i in range(dif-1, -1, -1):
					resp = strA[i] + resp
			else:	
				for i in range(dif-1, -1, -1):
					resp = strB[i] + resp				

		#print (resp)
		resp2 = int(resp, base=2)
		print (resp2)
	except :
		break
