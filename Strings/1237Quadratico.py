while True:
	try:
		u = input()
		v = input()
		tamU = len(u)
		tamV = len(v)
		resposta = 0
		i = 0
		j = tamV - 1
		r2 = [0]*tamU

		while (i < tamU):
			h = 0 # para andar nos vetores
			r = 0 # reposta
			p = i
			#print("---------")

			while (i + h < tamU and j + h < tamV):
				if (u[i+h] == v[j+h]):
					r = r + 1
				else:
					p = p + 1
				#print(u[i+h], v[j+h], r, i, h)
				if (i + h + 1 == tamU or j + h + 1 == tamV or u[i+h] != v[j+h]):
					while (r > 0):
						if (r > r2[p]):
							r2[p] = r
						p = p + 1
						r = r - 1
				h = h + 1

			# Andando com os indices
			if (j > 0):
				j = j -1
			else:
				i = i + 1
		#print(r2)
		print(max(r2))
	except :
		break