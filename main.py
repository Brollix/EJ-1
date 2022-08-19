from random import randint

respuesta = 0
camiones = 0

limite_carga = 500  # KG
limite_naranjas_en_cajon = 100
limite_peso_naranja = [150, 350]

# Funcion ingresar naranjas, y calcular cantidad de cajones


def CalculadoraDeCajones(num):
    iterador = 1
    cajones = []
    cajon = []
    sobrantes = []
    for i in range(iterador):
        for j in range(num):
            peso = randint(limite_peso_naranja[0], limite_peso_naranja[1])
            if len(cajon) < 100 or peso <= 300:
                cajon.append(peso)
            elif sum(cajon) >= 30000:
                sobrantes.append(peso)
                iterador += 1

        cajones.append(cajon)
    print(cajones)
    del cajon

    suma_naranjas = 0
    suma_peso = 0
    for i in range(len(cajones)):
        suma_naranjas += len(cajones[i])
        suma_peso += sum(cajones[i])

    print("naranjas para exportar:", suma_naranjas)
    print("peso total:", str(suma_peso / 100), "Kg")
    print("cajones:", iterador)
    print("naranjas para jugo:", len(sobrantes))


def CalculadoraDeCamiones(naranjas):
    print(naranjas)

while respuesta != -1:
    respuesta = int(input("Ingresar cantidad de naranjas: "))
    naranjas = respuesta

    CalculadoraDeCajones(naranjas)
