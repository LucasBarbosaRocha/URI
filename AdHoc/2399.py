# -*- coding: utf-8 -*-

def main():

    X = int(input())
    numeros = []
    minas = []

    for i in range(X):
        numero = int(input())
        numeros.append(numero)

    for i in range(X):
        contagem = 0

        if i == 0:
            if numeros[i] == 1:
                contagem = contagem + 1
            if i+1 < X and numeros[i+1] == 1:
                contagem = contagem + 1
        elif i == X - 1:
            if numeros[i] == 1:
                contagem = contagem + 1
            if numeros[i - 1] == 1:
                contagem = contagem + 1
        else:
            if numeros[i-1] == 1:
                contagem = contagem + 1
            if numeros[i] == 1:
                contagem = contagem + 1
            if i+1 < X and numeros[i+1] == 1:
                contagem = contagem + 1
        minas.append(contagem)

    for mina in minas:
        print(mina)


if __name__ == '__main__':
    main()