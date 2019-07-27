def cria_grafo(lista_de_vertices, lista_de_arestas):
    grafo = {}
    for vertice in lista_de_vertices:
        grafo[vertice] = []
    for aresta in lista_de_arestas:
        grafo[aresta[0]].append(aresta[1])
    return grafo





lista_de_vertices = ['a', 'b', 'c', 'd', 'e', 'f']
lista_de_arestas = [('a', 'b'), ('b', 'a'), ('b', 'c'), ('c', 'b'), ('c', 'e'), ('e', 'a'), ('e', 'b'), ('e', 'c'), ('e', 'd'), ('d', 'a'), ('d', 'e'), ('e', 'f'), ('f', 'e'), ('b', 'e'), ('a', 'd'), ('a', 'e')]
grafo = cria_grafo(lista_de_vertices, lista_de_arestas)
print grafo