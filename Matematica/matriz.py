import random
 
def criaMatriz(lin,col):
    A = []
    for i in range(lin):
        linha = []
        for j in range(col):
            linha = linha + [random.randint(1,10)]
        A = A +[linha]
    return A
 
if __name__ == "__main__":
    matriz = criaMatriz(2, 3)
    print (matriz)