def calcFat(n):
	if(n == 0):
		return 1
	return n * calcFat(n-1)

def calcFat2(n):
	s = 1
	for i in range(n,0,-1):
		s = s * i
	return s

while True:
	try:
		d = raw_input().split(" ")
		a = int(d[0])
		b = int(d[1])
		s = calcFat2(a) + calcFat2(b)
		print "%d" %(s)
	except:
		break
