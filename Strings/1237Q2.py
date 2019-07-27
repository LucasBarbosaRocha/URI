while True:
	try:
		p1 = input()
		p2 = input()
		m1 = len(p1)
		m2 = len(p2)
		resposta = 0
		for posP1 in range(m1):
			for posP2 in range(m2):

				if(p1[posP1] == p2[posP2]):
					r = 0
					h = 0
					while (posP1 + h < m1 and posP2 + h < m2):
						if(p1[posP1 + h] != p2[posP2 + h]):
							break
						h = h + 1
						r = r + 1
					if (r > resposta):
						resposta = r
		print(resposta)
	except :
		break