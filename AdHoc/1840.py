# -*- coding: utf-8 -*-

# Hash Map
naipes = {  "4": 1,
			"5": 2,
			"6": 3,
			"7": 4,
			"Q": 5,
			"J": 6,
			"K": 7,
			"A": 8,
			"2": 9,
			"3": 10	}

manilhas = {"4": "5",
			"5": "6",
			"6": "7",
			"7": "Q",
			"Q": "J",
			"J": "K",
			"K": "A",
			"A": "2",
			"2": "3",
			"3": "4"}

naipe = { 	"D": 1,
			"S": 2,
			"H": 3,
			"C": 4}

simbols = [1, 2, 3, 4]

# Recebe um naipe, verifica seu valor e retorna o maior
def MAX(A, B):
	if naipes[A] > naipes[B]:
		return A
	else:
		return B

def MAX2(A, B):
	if naipe[A] > naipe[B]:
		return A 
	else:
		return B

def MAX3(A, B):
	if A == "D":
		i = 0
	elif A == "S":
		i = 1
	elif A == "H":
		i = 2
	elif A == "C":
		i = 3

	if B == "D":
		j = 0
	elif B == "S":
		j = 1
	elif B == "H":
		j = 2
	elif B == "C":
		j = 3

	if simbols[i] > simbols[j]:
		return A
	else:
		return B


#naipes = ['4', '5', '6', '7', 'Q', 'J', 'K', 'A', '2', '3']
jogadas = [0, 0, 0, 0]


entrada = raw_input().split(" ")
n = int(entrada[0])
manilha = entrada[1]
manilhaE = manilhas[manilha[0]] # Carta de maior pontuacao


entrada = raw_input().split(" ")
p1 = entrada[0]
j1 = int(entrada[1])
entrada = raw_input().split(" ")
p2 = entrada[0]
j2 = int(entrada[1])
entrada = raw_input().split(" ")
p3 = entrada[0]
j3 = int(entrada[1])
entrada = raw_input().split(" ")
p4 = entrada[0]
j4 = int(entrada[1])

c1 = c2 = c3 = c4 = 0

for i in range(n):
	quemFez = ""
	entrada = raw_input().split(" ")

	jogada1 = entrada[0]
	jogada2 = entrada[1]
	jogada3 = entrada[2]
	jogada4 = entrada[3]

	aux1 = jogada1[0]
	n1 = jogada1[1]
	aux2 = jogada2[0]
	n2 = jogada2[1]
	aux3 = jogada3[0]
	n3 = jogada3[1]
	aux4 = jogada4[0]	
	n4 = jogada4[1]

	#Repetidos
	if aux1 == aux2:
		quemFez = aux1
		tmp = MAX3(n1, n2)
		if aux1 == aux3:
			tmp = MAX3(tmp, n3)
		if aux1 == aux4:
			tmp = MAX3(tmp, n4)
		if tmp == n2:
			quemFez = aux2				
		elif tmp == n3:
			quemFez = aux3				
		elif tmp == n4:
			quemFez = aux4				
	elif aux1 == aux3:
		quemFez = aux1
		tmp = MAX3(n1, n3)
		if aux1 == aux4:
			tmp = MAX3(tmp, n4)			
		if tmp == n3:
			quemFez = aux3				
		elif tmp == n4:
			quemFez = aux4			
	elif aux1 == aux4:
		quemFez = aux1
		tmp = MAX3(n1, n4)
		if aux1 == aux4:
			tmp = MAX3(tmp, n4)						
		if tmp == n4:
			quemFez = aux4	
	elif aux2 == aux3:
		quemFez = aux2
		tmp = MAX3(n2, n3)
		if aux2 == aux4:
			tmp = MAX3(tmp, n4)			
		if tmp == n3:
			quemFez = aux3				
		elif tmp == n4:
			quemFez = aux4
	elif aux2 == aux4:
		quemFez = aux2
		tmp = MAX3(n2, n4)			
		if tmp == n4:
			quemFez = aux4					
	#elif aux3 == aux4:
	#	quemFez = aux3
	#	tmp = MAX3(n3, n4)			
	#	if tmp == n4:
	#		quemFez = aux4	

	# Nao repetidos
	if quemFez == "":
		quemFez = MAX(aux1, aux2)
		quemFez = MAX(quemFez, aux3)
		quemFez = MAX(quemFez, aux4)
	else:
		quemFez = MAX(quemFez, aux1)
		quemFez = MAX(quemFez, aux2)
		quemFez = MAX(quemFez, aux3)
		quemFez = MAX(quemFez, aux4)

	if quemFez == aux1:
		quemFez = quemFez + n1
	elif quemFez == aux2:
		quemFez = quemFez + n2
	elif quemFez == aux3:
		quemFez = quemFez + n3
	elif quemFez == aux4:
		quemFez = quemFez + n4

	# Quando tiver a manilha
	if aux1 == manilhaE:
		quemFez = aux1 + n1
		if aux2 == manilhaE:
			tmp = MAX3(n1, n2)
			if tmp == n2:
				quemFez = aux2 + n2
		elif aux3 == manilhaE:
			tmp = MAX3(n1, n3)
			if tmp == n3:
				quemFez = aux3 + n3
		elif aux4 == manilhaE:
			tmp = MAX3(n1, n4)
			if tmp == n4:
				quemFez = aux4 + n4
	elif aux2 == manilhaE:
		quemFez = aux2 + n2
		if aux3 == manilhaE:
			tmp = MAX3(n2, n3)
			if tmp == n3:
				quemFez = aux3 + n3
		elif aux4 == manilhaE:
			tmp = MAX3(n2, n4)
			if tmp == n4:
				quemFez = aux4 + n4
	elif aux3 == manilhaE:
		quemFez = aux3 + n3
		if aux4 == manilhaE:
			tmp = MAX3(n3, n4)
			if tmp == n4:
				quemFez = aux4 + n4
	elif aux4 == manilhaE:
		quemFez = aux4 + n4

	if quemFez == jogada1:
		c1 = c1 + 1
	elif quemFez == jogada2:
		c2 = c2 + 1
	elif quemFez == jogada3:
		c3 = c3 + 1
	elif quemFez == jogada4:
		c4 = c4 + 1

	#print "---------"
	#print "quem fez "
	#print quemFez
	#print "Vitorias "
	#print c1, c2, c3, c4

vencedor = 0
if abs(j1-c1) == 0:
	vencedor = vencedor + 1
if abs(j2-c2) == 0:
	vencedor = vencedor + 1
if abs(j3-c3) == 0:
	vencedor = vencedor + 1
if abs(j4-c4) == 0:
	vencedor = vencedor + 1

if vencedor != 1:
	print "*"
else:
	if abs(j1-c1) == 0:
		print p1
	elif abs(j2-c2) == 0:
		print p2
	elif abs(j3-c3) == 0:
		print p3
	elif abs(j4-c4) == 0:
		print p4