
def verificar():
    return 0


def main():

    while True:
        X = int(input())

        if (X == 0):
            break
        
        numeros = list(map(int, input().split()))
        picos = 0
        
        if len(numeros) == X:
            
            for i in range(X):
                notaAtual = numeros[i]
                notaAntes = 0
                notaDepois = 0

                if i == 0:
                    notaAntes = numeros[X - 1]
                    notaDepois = numeros[i+1]
                elif i == X - 1:
                    notaAntes = numeros[X - 2]
                    notaDepois = numeros[0]
                else:
                    notaAntes = numeros[i-1]
                    notaDepois = numeros[i+1]
                
                if notaDepois > notaAtual and notaAntes > notaAtual:
                    picos = picos + 1
                elif notaDepois < notaAtual and notaAntes < notaAtual:
                    picos = picos + 1
        
        print(picos)

if __name__ == '__main__':
    main();