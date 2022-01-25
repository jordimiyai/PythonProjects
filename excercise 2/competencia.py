# Importamos librerías que vamos a utilizar
import random
from estadisticas import promedio_rondas
from enfrentamiento import *
from utiles import validar_tipo_carga


# genera los puntajes de manera aleatoria
def generar_puntos_auto():
    puntos_a = random.randint(1, 200)
    puntos_b = random.randint(1, 200)

    # en el caso que se asigne el mismo puntaje aplicamos un ciclo
    # de desempate con puntaje aleatorio
    while puntos_a == puntos_b:
        puntos_a += random.randint(1, 10)
        puntos_b += random.randint(1, 10)

    return puntos_a, puntos_b


def validar_positivo(nro):
    while nro < 0:
        nro = int(input('Error. Ingrese un número positivo: '))

    return nro


def generar_puntos_manual():
    puntos_a = puntos_b = 0
    empate = True

    while empate:
        puntos_a = int(input('Puntos A :'))
        puntos_a = validar_positivo(puntos_a)

        puntos_b = int(input('Puntos B :'))
        puntos_b = validar_positivo(puntos_b)

        if puntos_a == puntos_b:
            print('Empate. Ingrese puntajes distintos.')
        else:
            empate = False

    return puntos_a, puntos_b


# Carga los puntajes obtenidos al registro de enfrentamientos
def simular_competencia(ronda):
    n = len(ronda)
    tipo = validar_tipo_carga()

    for i in range(n):
        if tipo in 'aA':
            puntos_a, puntos_b = generar_puntos_auto()

        else:
            print('Enfrentamiento [' + str(i + 1) + ']')
            puntos_a, puntos_b = generar_puntos_manual()
            print()

        ronda[i].puntos1, ronda[i].puntos2 = puntos_a, puntos_b


# Arma el vector de la ronda que corresponda según los datos recibidos
def armar_cruces(competidores_ronda):
    n = len(competidores_ronda)
    m = n // 2
    v_ronda = [None] * m

    for j in range(m):
        v_ronda[j] = Enfrentamiento(competidores_ronda[j], competidores_ronda[n - 1 - j])

    return v_ronda


# Mostramos el fixture con los cruces
def mostrar_fixture(competidores_ronda):
    for i in range(len(competidores_ronda)):
        print(competidores_ronda[i].fixture())


# Mostramos la competencia con los puntajes por ronda
def mostrar_competencia(v_competidores):
    for i in range(len(v_competidores)):
        print('{:^80}'.format('~ * ' * 4 + 'RONDA ' + str(i + 1) + ' * ~' * 4))
        print('{:<15}{:>15}{:^20}{:<15}{:>15}'.format('Competidor A', 'Puntos', '|',
                                                      'Puntos', 'Competidor B'))
        print(v_competidores[i].to_string())
        print()


# genera el vector con los concursantes que pasan a la ronda siguiente
def obtener_ganadores(ronda):
    n = len(ronda)
    ganadores = [None] * n

    for i in range(n):
        ganadores[i] = ronda[i].ganador()

    return ganadores


# genera el vector de los participantes de semininal que compiten por el tercer puesto
def obtener_perdedores(ronda):
    n = len(ronda)
    perdedores = [None] * n

    for i in range(n):
        perdedores[i] = ronda[i].perdedor()

    return perdedores


def ronda(competidores_ronda, estadistica=True):

    # creamos los enfrentamientos de la ronda
    ronda = armar_cruces(competidores_ronda)

    # mostramos los enfrentamientos
    mostrar_fixture(ronda)

    # simulamos cada enfrentamiento y los mostramos
    simular_competencia(ronda)

    # mostramos el enfrentamiento
    mostrar_competencia(ronda)

    if estadistica:
        print()
        # generamos y mostramos los promedios
        print('{:^80}'.format('~* Estadisticas de la ronda. *~'))
        promedio_rondas(ronda)

    return ronda
