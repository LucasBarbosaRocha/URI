# -*- coding: utf-8 -*-
# Versão 2 usando matriz de adj.

# Funcao que cria uma matriz
def criaMatriz(lin,col):
    A = []
    for i in range(lin):
        linha = []
        for j in range(col):
            linha = linha + [0]
        A = A +[linha]
    return A

# Busca em profundidade personalizada
def dfs_iterative(grafo, i, n):
	stack = [i]
	cores = [-1]*(n+1)
	cores[i] = 1
	while stack:
		vertice = stack.pop()
		for adjacencia in grafo[vertice]:
			if (cores[adjacencia] == -1): # Em y (adjacencias) eh a cor invertida da cor do pai
				cores[adjacencia] = 1 - cores[vertice]
				stack.append(adjacencia) # Coloco a adjacencia na pilha
			elif (cores[adjacencia] == cores[vertice]): # Se a adjacencia tiver a mesma cor que o pai nao eh bipartido
				return False	
	return True



k = 1
while True:
	try:
		entrada = input().split(" ")
		n = int(entrada[0])
		m = int(entrada[1])
		verfices = []
		for i in range(1, n + 1):
			verfices.append(i)
		grafo = []
		cores = [-1]*(n+1)

		print ("Instancia %d" %k)
		# Verificar se o grafo eh bipartido
		grafo = criaMatriz(n, n)
		val = 0
		for i in range(m): 					
			entrada = input().split(" ")
			v1 = int(entrada[0])
			v2 = int(entrada[1])

			grafo[v1-1][v2-1] = 1

		if (myDFS(grafo, cores, n)):
			print ("sim")
		else:
			print ("nao")
	
		k = k + 1
		print()
	except :
		break
