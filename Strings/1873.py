n = int(input())
for i in range(n):
	entrada = input().split(" ")
	r = entrada[0]
	s = entrada[1]

	if (r == s):
		print("empate")
	elif (r == "tesoura" and s == "papel"):
		print("rajesh")
	elif (r == "papel" and s == "tesoura"):
		print("sheldon")
	elif (r == "papel" and s == "pedra"):
		print("rajesh")
	elif (r == "pedra" and s == "papel"):
		print("sheldon")
	elif (r == "pedra" and s == "lagarto"):
		print("rajesh")
	elif (r == "lagarto" and s == "pedra"):
		print("sheldon")
	elif (r == "lagarto" and s == "spock"):
		print("rajesh")
	elif (r == "spock" and s == "lagarto"):
		print("sheldon")
	elif (r == "spock" and s == "tesoura"):
		print("rajesh")
	elif (r == "tesoura" and s == "spock"):
		print("sheldon")
	elif (r == "tesoura" and s == "lagarto"):
		print("rajesh")
	elif (r == "lagarto" and s == "tesoura"):
		print("sheldon")
	elif (r == "lagarto" and s == "papel"):
		print("rajesh")
	elif (r == "papel" and s == "lagarto"):
		print("sheldon")
	elif (r == "papel" and s == "spock"):
		print("rajesh")
	elif (r == "spock" and s == "papel"):
		print("sheldon")
	elif (r == "spock" and s == "pedra"):
		print("rajesh")
	elif (r == "pedra" and s == "spock"):
		print("sheldon")
	elif (r == "pedra" and s == "tesoura"):
		print("rajesh")
	elif (r == "tesoura" and s == "pedra"):
		print("sheldon")