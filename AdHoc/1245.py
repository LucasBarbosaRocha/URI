while True:
	try:
		n = int(input())
		sapatos = [0]*62
		qtd = 0
		for i in range(n):
			entrada = input().split(" ")
			if (entrada[1] == "D"):
				pos = int(entrada[0])
				sapatos[pos + 1] = sapatos[pos + 1] + 1
				if (sapatos[pos - 30] > 0):
					qtd = qtd + 1
					sapatos[pos - 30] = sapatos[pos - 30] - 1
					sapatos[pos + 1] = sapatos[pos + 1] - 1
			else:
				pos = int(entrada[0])
				sapatos[pos - 30] = sapatos[pos - 30] + 1
				if (sapatos[pos + 1] > 0):
					qtd = qtd + 1
					sapatos[pos + 1] = sapatos[pos + 1] - 1
					sapatos[pos - 30] = sapatos[pos - 30] - 1
		print (qtd)
		#print (sapatos)
	except :
		break


