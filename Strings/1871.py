while True:

	entrada = input().split(" ")
	m = int(entrada[0])
	n = int(entrada[1])
	if (m == 0 and n == 0):
		break
	soma = m + n
	resultado = str(soma)
	result = ""
	tam = len(resultado)
	for i in range(tam):
		if (resultado[i] != '0'):
			result = result + resultado[i]
	print (result)
