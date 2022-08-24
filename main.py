from random import randint as rand

num = int(input('cantidad de números a ingresar: '))
low = int(input('numero random minimo: '))
high = int(input('numero random máximo: '))

arr = []
for i in range(num):
    arr.append(rand(low, high))


def normalizar(lista):
    print('Números normalizados:')
    suma = sum(lista)
    for i in range(len(lista)):
        lista[i] /= suma
        # lista[i] = round(lista[i], 2)

    print(lista)
    print(f'suma de los valores normalizados: "{round(sum(lista), 2)}"')


normalizar(arr)
