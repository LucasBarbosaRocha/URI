while True:
	try:
		entrada = input()
		tam = len(entrada)
		palavra = ""
		for i in range(tam):
			if (entrada[i] == " "):
				palavra = palavra + " "
			else:
				palavra = palavra + chr(ord(entrada[i]) - 6)
		print (palavra)
	except :
		break