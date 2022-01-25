# Importamos librerías que vamos a utilizar
from estadisticas import *
from carga_de_datos import carga_competidores
from competencia import *
from utiles import pausar

# ordenamos los competidores por el ranking
def ordenar_competidores(v_competidores):
    n = len(v_competidores)

    for j in range(1, n):
        competidor = v_competidores[j]
        ant = j - 1

        # verificamos las posiciones anteriores e intercambiamos las que sean necesarias
        while ant >= 0 and v_competidores[ant].ranking < competidor.ranking:
            v_competidores[ant + 1] = v_competidores[ant]
            ant -= 1

        v_competidores[ant + 1] = competidor

    return


# mostramos los datos de los competidores
def mostrar_competidores(v_competidores):
    n = len(v_competidores)

    for i in range(n):
        print('{:^80}'.format('~* Participante [' + str(i+1) + '] *~'))
        print(v_competidores[i].to_string())
        print()


def principal():

    print('{:^80}'.format('Bienvenido al sistema de gestion de competencias.'))
    print()

    # creamos el vector que va a contener los registros
    competidores = 16 * [None]

    # cargamos los datos
    carga_competidores(competidores)

    # ordenamos el vector segun el ranking
    ordenar_competidores(competidores)
    print()
    print('Los competidores, ordenados según su ranking, son:\n')

    # mostramos los competidores ordenados
    mostrar_competidores(competidores)

    # generamos y mostramos la primera estadistica solicitada
    contador = contar_continente(competidores)
    print('{:^80}'.format('~* Estadísticas de la ronda. *~'))
    mostrar_contador(contador)

    pausar()

    # comienzan las rondas
    print('{:^80}'.format('~ * ' * 5 + 'OCTAVOS DE FINAL' + ' * ~' * 5 + '\n'))

    octavos = ronda(competidores)
    competidores_a_cuartos = obtener_ganadores(octavos)

    pausar()
    print('{:^80}'.format('~ * ' * 5 + 'CUARTOS DE FINAL' + ' * ~' * 5 + '\n'))

    # volvemos a invocar a las funciones para armar cuartos
    cuartos = ronda(competidores_a_cuartos)
    competidores_a_semi = obtener_ganadores(cuartos)

    pausar()

    print('{:^80}'.format('~ * ' * 5 + 'SEMIFINAL' + ' * ~' * 5 + '\n'))

    # volvemos a invocar a las funciones para armar semifinal
    semifinal = ronda(competidores_a_semi)
    competidores_a_final = obtener_ganadores(semifinal)

    pausar()
    print('{:^80}'.format('~ * ' * 5 + 'TERCER PUESTO' + ' * ~' * 5 + '\n'))

    # armamos la ronda por el tercer puesto
    competidores_tercer_puesto = obtener_perdedores(semifinal)
    tercero = ronda(competidores_tercer_puesto, False)

    pausar()

    print('{:^80}'.format('~ * ' * 5 + 'FINAL' + ' * ~' * 5 + '\n'))

    # volvemos a invocar a las funciones para armar la Final
    final = ronda(competidores_a_final, False)

    pausar()
    print('{:^80}'.format('~ * ' * 5 + 'PODIO' + ' * ~' * 5 + '\n'))

    # creamos y mostramos el podio con ranking sin modificar
    podio = crear_podio(final, tercero)
    mostrar_podio(podio)
    print()

    # modificamos el ranking
    modificar_rankings(podio)

    # ordenamos según el nuevo ranking
    ordenar_competidores(competidores)

    pausar()
    print('{:^80}'.format('~ * ' * 5 + 'NUEVO RANKING' + ' * ~' * 5 + '\n'))



    # mostramos nuevamente el ranking actualizado
    mostrar_competidores(competidores)

    print('~ * Fin de la competencia * ~')

    return


if __name__ == '__main__':
    principal()
