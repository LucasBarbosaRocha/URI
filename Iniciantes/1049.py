p1 = raw_input()
p2 = raw_input()
p3 = raw_input()


if p1 == "vertebrado" :
	if p2 == "ave" :
		if p3 == "carnivoro" :
			print "aguia"
		else:
			print "pomba"
	else:
		if p3 == "onivoro" :
			print "homem"
		else:
			print "vaca"
else:
	if p2 == "inseto" :
		if p3 == "hematofago" :
			print "pulga"
		else:
			print "lagarta"
	else:
		if p3 == "hematofago" :
			print "sanguessuga"
		else:
			print "minhoca"
