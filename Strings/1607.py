alfabeto = {
	"a": 0, "b": 1,"c": 2, "d": 3,"e": 4, "f": 5,
	"g": 6, "h": 7,"i": 8, "j": 9,"k": 10, "l": 11,
	"m": 12, "n": 13,"o": 14, "p": 15,"q": 16, "r": 17,
	"s": 18,"t": 19, "u": 20,"v": 21, "w": 22, "x": 23, 
	"y": 24,"z": 25
}

n = int(input())

while n > 0:
	entrada = input().split(" ")
	a = entrada[0]
	b = entrada[1]
	tam = len(a)

	r = 0
	for i in range(tam):
		ordA = ord(a[i])
		ordB = ord(b[i])
		if (ordA < ordB):
			r = r + (ordB - ordA)
		elif (ordA > ordB):
			#print (r, alfabeto[b[i]], alfabeto[a[i]])
			r = r + ((25 - alfabeto[a[i]]) + alfabeto[b[i]] + 1)
	print (r)
	n = n - 1