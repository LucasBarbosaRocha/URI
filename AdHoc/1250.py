num = int(raw_input())
while num > 0:
	cont = 0
	i = 0
	tiros = int(raw_input())
	todosTiros = raw_input().split(" ")
	todosPulos = raw_input()

	for i in range(tiros):
		if (todosTiros[i] == '1' or todosTiros[i] == '2') and todosPulos[i] == 'S':
			cont = cont + 1
		elif (todosTiros[i] > '2' and todosPulos[i] == 'J'):
			cont = cont + 1
	print cont
	num = num - 1