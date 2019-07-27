# -*- coding: utf-8 -*-
n = input()

while n > 0:
	scan = raw_input()
	tam = len(scan)
	r = ""
	for i in range((tam/2)-1, -1, -1):
		r = r + scan[i]
	for i in range(tam-1, (tam/2)-1, -1):
		r = r + scan[i]
	print r
	n = n - 1