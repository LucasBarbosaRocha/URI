def euclides_mdc(dividendo, divisor): # Maximo divisor comum pelo metodo de euclides
    while divisor != 0:
        temp = divisor
        divisor = dividendo % divisor
        dividendo = temp    
    return dividendo


while True:	
	try:
		entrada = raw_input().split(" ")

		azul = int(entrada[0])
		preta = int(entrada[1])
		equipes = int(entrada[2])

		tam = euclides_mdc(azul, preta) # Tamanho do pacote
		pacotes = (azul+preta)/tam # qtd Pacotes

		if pacotes >= equipes:
			print "sim"
		else:
			print "nao"
	except:
		break