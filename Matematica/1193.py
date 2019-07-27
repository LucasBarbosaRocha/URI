n = int(input())

for i in range(n):
	entrada = input().split(" ")
	number = entrada[0]
	tipo = entrada[1]

	print ("Case %d:" %(i+1))

	if (tipo == "bin"):
		#decimal
		dec = 0
		elev = 0
		for j in range(len(number) - 1, -1, -1):
			dec = dec + ((2**elev)*int(number[j]))
			elev = elev + 1
		#hexa
		hexa = 0
		respostaHexa = ""
		j = len(number) - 1
		while j >= 0:
			k = 0
			hexa = 0
			elev = 0
			while j > - 1 and k < 4:
				hexa = hexa + ((2**elev)*int(number[j]))
				elev = elev + 1				
				k = k + 1
				j = j - 1
			if (hexa == 10):
				respostaHexa = "a" + respostaHexa
			elif (hexa == 11):
				respostaHexa = "b" + respostaHexa
			elif (hexa == 12):
				respostaHexa = "c" + respostaHexa
			elif (hexa == 13):
				respostaHexa = "d" + respostaHexa
			elif (hexa == 14):
				respostaHexa = "e" + respostaHexa
			elif (hexa == 15):
				respostaHexa = "f" + respostaHexa
			else:
				respostaHexa = str(hexa) + respostaHexa
		print ("%d dec" %dec)
		print ("%s hex" %respostaHexa)
	elif (tipo == "dec"):
		#hex
		hexa = int(int(number) / 16)
		resto = int(number) % 16
		respostaHexa = ""
		while (hexa != 0):
			if (resto == 10):
				respostaHexa = respostaHexa + "a" 
			elif (resto == 11):
				respostaHexa = respostaHexa + "b"
			elif (resto == 12):
				respostaHexa = respostaHexa + "c"
			elif (resto == 13):
				respostaHexa = respostaHexa + "d"
			elif (resto == 14):
				respostaHexa = respostaHexa + "e"
			elif (resto == 15):
				respostaHexa = respostaHexa + "f"
			else:
				respostaHexa = respostaHexa +  str(resto)
			resto = hexa % 16
			hexa = int(hexa / 16)
		if (resto == 10):
			respostaHexa = respostaHexa + "a" 
		elif (resto == 11):
			respostaHexa = respostaHexa + "b"
		elif (resto == 12):
			respostaHexa = respostaHexa + "c"
		elif (resto == 13):
			respostaHexa = respostaHexa + "d"
		elif (resto == 14):
			respostaHexa = respostaHexa + "e"
		elif (resto == 15):
			respostaHexa = respostaHexa + "f"
		else:
			respostaHexa = respostaHexa +  str(resto)

		# binario
		bina = int(int(number) / 2)
		resto = int(number) % 2
		respostaBina = ""
		while (bina != 0):
			respostaBina = respostaBina + str(resto)
			resto = bina % 2
			bina = int(bina / 2)
		respostaBina = respostaBina + str(resto)
		print("%s hex" %respostaHexa[::-1])
		print("%s bin" %respostaBina[::-1])
	else :
		number = number.upper()
		tam = len(number)
		dec = 0
		elev = 0
		for j in range(tam - 1, -1, -1):
			if (number[j] == "A"):
				n = 10
			elif (number[j] == "B"):
				n = 11
			elif (number[j] == "C"):
				n = 12
			elif (number[j] == "D"):
				n = 13
			elif (number[j] == "E"):
				n = 14
			elif (number[j] == "F"):
				n = 15
			else:
				n = int(number[j])
			dec = dec + (n*(16**elev))
			elev = elev + 1
		# binario
		bina = ""
		for j in range(tam):
			if (number[j] == "1"):
				bina = bina + "0001"
			elif (number[j] == "2"):
				bina = bina + "0010"
			elif (number[j] == "3"):
				bina = bina + "0011"
			elif (number[j] == "4"):
				bina = bina + "0100"
			elif (number[j] == "5"):
				bina = bina + "0101"
			elif (number[j] == "6"):
				bina = bina + "0110"
			elif (number[j] == "7"):
				bina = bina + "0111"
			elif (number[j] == "8"):
				bina = bina + "1000"
			elif (number[j] == "9"):
				bina = bina + "1001"
			elif (number[j] == "A"):
				bina = bina + "1010"
			elif (number[j] == "B"):
				bina = bina + "1011"
			elif (number[j] == "C"):
				bina = bina + "1100"
			elif (number[j] == "D"):
				bina = bina + "1101"
			elif (number[j] == "E"):
				bina = bina + "1110"
			elif (number[j] == "F"):
				bina = bina + "1111"
		print ("%d dec" %dec)
		print ("%s bin" %bina)
	print ()
