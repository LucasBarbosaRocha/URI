resposta = ""
while True:
	try:
		entrada = input().split(" ")
		tam = len(entrada)
		for i in range(tam):
			#print ("VAmos começar com %s" %entrada)
			#print ("ANALISE %s" %entrada[i])
			if (i == tam - 1):
				nova = entrada[i] + " "
			else:
				nova = entrada[i]

			if (entrada[i] != ''):
				if ("<br>" in entrada[i]):
					p = entrada[i]
					if (len(p) == 4):
						if (resposta != ""):
							print(resposta)
							resposta = ""
						else:
							print()
				elif ("<hr>" in entrada[i]):
					p = entrada[i]
					if (len(p) == 4):
						if (resposta != ""):
							print(resposta)
							resposta = ""
							print ("--------------------------------------------------------------------------------")
						else:
							print ("--------------------------------------------------------------------------------")
				elif (len(resposta+" "+nova) < 81):
					if (not resposta):
						resposta = resposta + entrada[i]
					else:
						resposta = resposta +" "+ entrada[i]
					#print ("Resposta: %s entrada: %s tamanho: %d" %(resposta, entrada[i], len(resposta+" "+entrada[i])))
				elif (len(resposta+" "+nova) >= 81):
					print (resposta)
					resposta = entrada[i]
		#print (entrada)
	except :
		break

if (resposta != " "):
	print (resposta)