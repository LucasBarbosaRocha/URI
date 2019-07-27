while True:
	try:
		entrada = input("")
		if (entrada == ""):
			print()
		else:
			entrada = entrada.replace(" ","")
			ordenada = ''.join(sorted(entrada)) + "$"
			intervalos = []
			first = 1
			intervalo = ""
			for i in range(len(ordenada)):
				if (first == 1):
					intervalo = ordenada[i]
					first = 2
				else:
					if (ordenada[i-1] != ordenada[i] and ord(ordenada[i-1]) - ord(ordenada[i]) != -1):
						intervalo = intervalo + ":" + ordenada[i-1]
						intervalos.append(intervalo)
						intervalo = ordenada[i]
			if (len(intervalos) > 1):
				for i in range(len(intervalos)):
					if(i < len(intervalos) - 1):
						print("%s, " %intervalos[i], end='')
					else:
						print("%s" %intervalos[i])					
			else:
				print(intervalos[0])
	except :	
		break