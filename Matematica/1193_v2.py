n = int(input())

for i in range(n):
	entrada = input().split(" ")
	number = entrada[0]
	tipo = entrada[1]

	print ("Case %d:" %(i+1))

	if (tipo == "bin"):
		dec = int(number, base=2)
		hexa = hex(int(number, base=2))
		print ("%s dec" %dec)
		print ("%s hex" %hexa[2:])
	elif (tipo == "dec"):
		bina = bin(int(number, base=10))
		hexa = hex(int(number, base=10))
		print ("%s hex" %hexa[2:])
		print ("%s bin" %bina[2:])
	elif (tipo == "hex"):
		dec = int(number, base=16)
		bina = bin(int(number, base=16))
		print ("%s dec" %dec)
		print ("%s bin" %bina[2:])
	print ()