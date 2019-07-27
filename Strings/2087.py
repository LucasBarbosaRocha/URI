while True:
	n = int(input())
	if (n == 0):
		break
	palavraBKP = ""
	cont = 1
	for i in range(n):
		palavra = input()
		if (i == 0):
			palavraBKP = palavra
		else:
			if (palavra in palavraBKP or palavraBKP in palavra):
				cont = cont + 1
