n = int(input())
nomeA = ""
poderA = 0
matouA = 0
morreuA = 0

for i in range(n):
	entrada = input().split(" ")
	if (i == 0):
		nomeA = entrada[0]
		poderA = int(entrada[1])
		matouA = int(entrada[2])
		morreuA = int(entrada[3])
	else:
		nome = entrada[0]
		poder = int(entrada[1])
		matou = int(entrada[2])
		morreu = int(entrada[3])

		if (poder > poderA):
			nomeA = entrada[0]
			poderA = int(entrada[1])
			matouA = int(entrada[2])
			morreuA = int(entrada[3])
		elif (poder == poderA):
			if (matou > matouA):
				nomeA = entrada[0]
				poderA = int(entrada[1])
				matouA = int(entrada[2])
				morreuA = int(entrada[3])
			elif (matou == matouA):
				if (morreu < morreuA):
					nomeA = entrada[0]
					poderA = int(entrada[1])
					matouA = int(entrada[2])
					morreuA = int(entrada[3])
				elif (morreu == morreuA):
					if (len(nome) < len(nomeA)):
						nomeA = entrada[0]
						poderA = int(entrada[1])
						matouA = int(entrada[2])
						morreuA = int(entrada[3])
					else:		
						nomeA = nome
						poderA = poder
						matouA = matou
						morreuA = morreu
print(nomeA)



