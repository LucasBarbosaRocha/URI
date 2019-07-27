while True:
	try:
		entrada = input()
		aux = ""
		r2 = entrada
		tam = len(entrada)
		for i in range(tam):
			if(r2[i] >= '0' and r2[i] <= '9'):
				aux = aux + r2[i]
			elif(r2[i] == '*'):
				aux = aux + '*'
			elif(r2[i] == "#"):
				aux = aux + '#'
			elif(r2[i] >= 'A' and r2[i] <= 'C'):
				aux = aux + '2'
			elif(r2[i] >= 'D' and r2[i] <= 'F'):
				aux = aux + '3'
			elif(r2[i] >= 'G' and r2[i] <= 'I'):
				aux = aux + '4'
			elif(r2[i] >= 'J' and r2[i] <= 'L'):
				aux = aux + '5'
			elif(r2[i] >= 'M' and r2[i] <= 'O'):
				aux = aux + '6'
			elif(r2[i] >= 'P' and r2[i] <= 'S'):
				aux = aux + '7'
			elif(r2[i] >= 'T' and r2[i] <= 'V'):
				aux = aux + '8'
			elif(r2[i] >= 'W' and r2[i] <= 'Z'):
				aux = aux + '9'
		print(aux)
	except :
		break