entrada = raw_input().split(" ")

t1 = int(entrada[0])
t2 = int(entrada[1])
t3 = int(entrada[2])

if t1 > t2 and t2 <= t3:
	print ":)"
elif t1 < t2 and t2 >= t3:
	print ":("
elif t1 < t2 and t2 < t3 and ((t2-t1) > (t3-t2)):
	print ":("
elif t1 < t2 and t2 < t3 and (t2-t1) <= (t3-t2):
	print ":)"
elif t1 > t2 and t2 > t3 and (t1-t2) > (t2-t3):
	print ":)"
elif t1 > t2 and t2 > t3 and (t1-t2) <= (t2-t3):
	print ":("
elif t2 == t1 and t2 < t3:
	print ":)"
else:
	print ":("