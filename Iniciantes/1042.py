def menor(a, b):
	if a < b:
		return a
	else:
		return b

entrada = raw_input().split(" ")
msg = ""

a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

aux = menor(menor(a,b),c)
if aux == a:
	tmp = menor(b,c)
	if tmp == b:
		msg = "%d\n%d\n%d" % (aux,tmp,c)
	else:
		msg = "%d\n%d\n%d" % (aux,tmp,b)
elif aux == b:
	tmp = menor(a,c)
	if tmp == a:
		msg = "%d\n%d\n%d" % (aux,tmp,c)
	else:
		msg = "%d\n%d\n%d" % (aux,tmp,a)
elif aux == c:
	tmp = menor(a,b)
	if tmp == a:
		msg = "%d\n%d\n%d" % (aux,tmp,b)
	else:
		msg = "%d\n%d\n%d" % (aux,tmp,a)
print msg

print ""

a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

msg = "%d\n%d\n%d" % (a,b,c)
print msg
