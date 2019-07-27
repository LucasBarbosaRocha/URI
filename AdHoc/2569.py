entrada = raw_input().split(" ")

n1 = entrada[0]
n2 = entrada[2]
op = entrada[1]

n1 = n1.replace("7", "0")
n2 = n2.replace("7", "0")

n1 = int(n1)
n2 = int(n2)

result = str(n1 + n2)
if op == 'x':
	result = str(n1 * n2)

result = result.replace("7", "0")

print int(result)