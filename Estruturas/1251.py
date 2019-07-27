past = 0
while True:
	try:
		entrada = input()
		tam = len(entrada)
		if (past == 1 and tam > 0):
			print ()

		dic = [0]*129

		for i in range(tam):
			value = ord(entrada[i])
			#print(value)
			dic[value] = dic[value] + 1
		a = dic[::-1]
		#print (a)
		l = []
		va = [0,0]
		for i in range(129):
			if (dic[i] != 0):
				va = i, dic[i]
				l.append(va)
		#print(l)
		l = sorted(l, key=lambda x: x[1])
		#print(l)
		tam = len(l)
		last = l[tam-1][1]
		#print (last)
		i = 1
		l2 = []
		j = 0
		while (j < tam and i <= last):
			#print (l[j][1], i)
			if (l[j][1] == i):
				l2.append(l[j])
			else :
				i = l[j][1]
				j = j - 1
				#print ("Novo i %d" %i)
				#print (l2)
				tam2 = len(l2)
				l2 = sorted(l2, key=lambda x: x[0], reverse=True)
				for k in range(tam2):
					print("%d %d" %(l2[k][0], l2[k][1]))
				l2 = []
			j = j + 1
		tam2 = len(l2)
		l2 = sorted(l2, key=lambda x: x[0], reverse=True)
		for k in range(tam2):
			print("%d %d" %(l2[k][0], l2[k][1]))
		past = 1
				



	except :
		break
