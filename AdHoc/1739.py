fibo1 = [0]*100
fibo2 = [0]*61
fibo1[0] = 1
fibo1[1] = 1

cont = 0
j = 0
i = 2
while (j < 61 and i < 100):
	fibo1[i] = fibo1[i-1] + fibo1[i-2]
	if (fibo1[i] % 3 == 0):
		cont = cont + 1
		fibo2[j] = fibo1[i]
		j = j + 1
	elif ('3' in str(fibo1[i])):
		cont = cont + 1
		fibo2[j] = fibo1[i]
		j = j + 1
	i = i + 1

while True:
	try:
		n = int(input())
		print(fibo2[n-1])
	except :
		break