def imprime(i, msg):
	print "Caso #%d: %s!" % (i, msg)

n = int(raw_input())
i = 1
while i <= n:

	entrada = raw_input().split(" ")

	# Sheldon ganhando
	if entrada[0] == "tesoura" and entrada[1] == "papel" :
		imprime(i, "Bazinga")
	elif entrada[0] == "papel" and entrada[1] == "pedra" :
		imprime(i, "Bazinga")
	elif entrada[0] == "pedra" and entrada[1] == "lagarto" :
		imprime(i, "Bazinga")
	elif entrada[0] == "lagarto" and entrada[1] == "Spock" :
		imprime(i, "Bazinga")
	elif entrada[0] == "Spock" and entrada[1] == "tesoura" :
		imprime(i, "Bazinga")
	elif entrada[0] == "tesoura" and entrada[1] == "lagarto" :
		imprime(i, "Bazinga")
	elif entrada[0] == "lagarto" and entrada[1] == "papel" :
		imprime(i, "Bazinga")
	elif entrada[0] == "papel" and entrada[1] == "Spock" :
		imprime(i, "Bazinga")
	elif entrada[0] == "Spock" and entrada[1] == "pedra" :
		imprime(i, "Bazinga")
	elif entrada[0] == "pedra" and entrada[1] == "tesoura" :
		imprime(i, "Bazinga")

	# Vitoria Raj
	if entrada[1] == "tesoura" and entrada[0] == "papel" :
		imprime(i, "Raj trapaceou")
	elif entrada[1] == "papel" and entrada[0] == "pedra" :
		imprime(i, "Raj trapaceou")
	elif entrada[1] == "pedra" and entrada[0] == "lagarto" :
		imprime(i, "Raj trapaceou")
	elif entrada[1] == "lagarto" and entrada[0] == "Spock" :
		imprime(i, "Raj trapaceou")
	elif entrada[1] == "Spock" and entrada[0] == "tesoura" :
		imprime(i, "Raj trapaceou")
	elif entrada[1] == "tesoura" and entrada[0] == "lagarto" :
		imprime(i, "Raj trapaceou")
	elif entrada[1] == "lagarto" and entrada[0] == "papel" :
		imprime(i, "Raj trapaceou")
	elif entrada[1] == "papel" and entrada[0] == "Spock" :
		imprime(i, "Raj trapaceou")
	elif entrada[1] == "Spock" and entrada[0] == "pedra" :
		imprime(i, "Raj trapaceou")
	elif entrada[1] == "pedra" and entrada[0] == "tesoura" :
		imprime(i, "Raj trapaceou")

	# Empate
	if entrada[1] == "tesoura" and entrada[0] == "tesoura" :
		imprime(i, "De novo")
	elif entrada[1] == "papel" and entrada[0] == "papel" :
		imprime(i, "De novo")
	elif entrada[1] == "pedra" and entrada[0] == "pedra" :
		imprime(i, "De novo")
	elif entrada[1] == "lagarto" and entrada[0] == "lagarto" :
		imprime(i, "De novo")
	elif entrada[1] == "Spock" and entrada[0] == "Spock" :
		imprime(i, "De novo")

	i = i + 1