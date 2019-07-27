def doPar(par, cont):
	val = 0
	i = 0
	j = len(par) - 1
	cont = 0
	while i < j:
		dif = par[j] - par[i]
		div = dif / 2
		par[j] = par[j] - div
		par[i] = par[i] + div
		if par[i] != par[j]:
			val = 1
			break
		i = i + 1
		j = j - 1
		cont = cont + div
	return [val, cont]

def doImpar(imp, cont):
	val = 0
	i = 0
	j = len(imp) - 1
	while i < j:
		dif = imp[j] - imp[i]
		div = dif / 2
		print "dif div"
		print dif, div
		imp[j] = imp[j] - div
		imp[i] = imp[i] + div
		if imp[i] != imp[j]:
			val = 1
		i = i + 1
		j = j - 1
		cont = cont + div
	return [val, cont]

def finalScan(imp):
	for i in range(len(imp)-1):
		if imp[i] != imp[i+1]:
			return 1
	return 0


n = input()
entrada = raw_input().split(" ")
par = []
imp = []
ve = []
for i in range(len(entrada)):
	aux = int(entrada[i])
	ve.append(aux)
	if aux % 2 == 0:
		par.append(aux)
	else:
		imp.append(aux)

cont = 0

for i in range(15):
	v = doPar(ve, cont)
	val = v[0]
	cont = v[1]
	ve.sort()
	print ve

val = finalScan(imp)

if val == 0:
	print cont
	print par, imp
else:
	print "-1"
	print par, imp