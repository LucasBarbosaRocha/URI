# -*- coding: utf-8 -*-

# Funcao que cria um grafo
def cria_grafo(lista_de_vs, lista_de_arestas):
    grafo = {}
    for v in lista_de_vs:
        grafo[v] = []
    for aresta in lista_de_arestas:
        grafo[aresta[0]].append(aresta[1])
    return grafo

# Busca em profundidade personalizada
def dfs_iterative(grafo, i, n, verticesValidos):
	cores = [-1]*(n+1)

	for j in range(i, n + 1):
		if (j in verticesValidos):
			stack = [j]
			cores[j] = 1
			while stack:
				v = stack.pop()
				#print ("BLABLA")
				#print (stack)
				for adjacencia in grafo[v]:
					if (cores[adjacencia] == -1): # Em y (adjacencias) eh a cor invertida da cor do pai
						cores[adjacencia] = 1 - cores[v]
						stack.append(adjacencia) # Coloco a adjacencia na pilha
					elif (cores[adjacencia] == cores[v]): # Se a adjacencia tiver a mesma cor que o pai nao eh bipartido
						return False
				verticesValidos.remove(v)
			#print (cores)	
	return True

k = 1
while True:
	try:
		entrada = raw_input().split(" ")
		n = int(entrada[0])
		m = int(entrada[1])
		vertices = []
		verticesValidos = []
		for i in range(1, n + 1):
			vertices.append(i)
		arestas = []
		grafo = []
		caminho = []
		totalArestas = 0
		print ("Instancia %d" %k)
		# Verificar se o grafo eh bipartido
		#print ("AQUI")
		#print(n, m)
		for i in range(m): 					
			entrada = raw_input().split(" ")
			v1 = int(entrada[0])
			v2 = int(entrada[1])


			if (verticesValidos == []):
				verticesValidos.append(v1)
				verticesValidos.append(v2)
			if (v1 not in verticesValidos):
				verticesValidos.append(v1)
			if (v2 not in verticesValidos):
				verticesValidos.append(v2)

			arestas.append((v1, v2))
			#arestas.append((v2, v1))

		
		grafo = cria_grafo(verticesValidos, arestas)	
		#print (grafo)		
		#print (verticesValidos)
		if (m == 0 or dfs_iterative(grafo, verticesValidos[0], n, verticesValidos) == True):
			print ("sim\n")
		else:
			print ("nao\n")


		k = k + 1
	except :
		break
