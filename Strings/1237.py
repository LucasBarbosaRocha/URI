while True:
	try:
		p1 = input()
		p2 = input()
		m1 = len(p1)
		m2 = len(p2)
		resposta = 0
		for posP1 in range(m1):
			for posP2 in range(m2):
				r = 0
				h = 0
				#print("--")
				while (posP1 + h < m1 and posP2 + h < m2):
					if(p1[posP1 + h] == p2[posP2 + h]):
						r = r + 1
					else:
						break
					h = h + 1
				#print(r, resposta)
				if (r > resposta):
					resposta = r
		print(resposta)
	except :
		break