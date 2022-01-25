def contar_continente(v_competidores):
    n = len(v_competidores)
    contador = [0] * 5

    for i in range(n):
        k = v_competidores[i].continente
        contador[k] += 1

    return contador


def mostrar_contador(contador):
    cont = ('América', 'Europa', 'Asia', 'África', 'Oceanía')

    print('\nEn la edición 2020 del campeonato contamos con: ')
    for i in range(len(contador)):
        print('\t- ', contador[i], ' participantes de ', cont[i])


# calculamos el promedio solicitado por las estadísticas
def calcular_promedio(ronda):
    n = len(ronda)
    acumulador = 0
    for i in range(n):
        acumulador += ronda[i].puntos1 + ronda[i].puntos2

    prom = 0
    if n != 0:
        prom = round(acumulador / (n * 2), 1)

    return prom


# muestra el promedio
def promedio_rondas(ronda):
    promedio = calcular_promedio(ronda)
    print('El promedio de puntajes en esta ronda fue de ', promedio, 'puntos.')
    print()


# asignamos al vector los registros correspondientes a los ganadores, según corresponda
def crear_podio(final, tercero):
    podio = [final[0].ganador(), final[0].perdedor(), tercero[0].ganador()]
    return podio


# imprime el podio
def mostrar_podio(podio):
    print('{:^80}'.format('~ * Campeon * ~\n'))
    print(podio[0].to_string())
    print()
    print('{:^80}'.format('~ * 2do Puesto * ~\n'))
    print(podio[1].to_string())
    print()
    print('{:^80}'.format('~ * 3er puesto  * ~\n'))
    print(podio[2].to_string())


# asignamos el puntaje correspondientes por puesto
def modificar_rankings(podio):
    aumentos = (25, 15, 5)

    for i in range(len(podio)):
        podio[i].ranking += aumentos[i]
