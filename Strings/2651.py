entrada = input()
entrada = entrada.lower()
tam = len(entrada)
zelda = "zelda"
v = 0
i = 0
j = 0
while (i < tam):
	j = 0
	while (i < tam and j < len(zelda) and entrada[i] == zelda[j]):
		i = i + 1
		j = j + 1
	if (j == len(zelda)):
		v = 1
		break
	i = i + 1

if (v == 1):
	print ("Link Bolado")
else :
	print ("Link Tranquilo")