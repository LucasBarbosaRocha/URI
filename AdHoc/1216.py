cont = 0
tmp = 0
while True:
    try:
	    nome = raw_input().split(" ")
	    distancia = int(raw_input())
	    cont = cont + 1
	    tmp = tmp + distancia
    except:
        break
print "%.1f" % (tmp/float(cont))