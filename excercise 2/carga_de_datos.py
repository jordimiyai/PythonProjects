# Importamos librerías que vamos a utilizar
from competidor import *
import random
from utiles import validar_tipo_carga


def validar_nombre(v_competidores):
    n = len(v_competidores)
    nombre = None
    repetido = False

    # entra al ciclo con nombre None o repetido
    while repetido or nombre is None:
        nombre = input('Nombre: ')
        repetido = False

        # recorre el vector
        for i in range(n):

            # ingresa solo si no está vacío y si está repetido
            if v_competidores[i] is not None and v_competidores[i].nombre == nombre:
                print('El nombre se encuentra repetido. Reingrese')

                # confirma que está repetido y corta el ciclo
                repetido = True
                break

    return nombre


def validar_continente():
    continente = int(input('Código del continente (0-América, 1-Europa, 2-Asia,'
                           ' 3-África, 4-Oceanía): '))

    # validamos que este en el rango
    while continente < 0 or continente > 4:
        continente = int(input('Error. Reingrese: '))

    return continente


def validar_ranking():
    ranking = int(input('Ranking: '))

    # validamos que sea positivo
    while ranking <= 0:
        ranking = int(input('Error. Ingrese un valor mayor a 0: '))
    return ranking


# se toma por teclado los datos de los concursantes validando según corresponda
def carga_manual(v_competidores):
    n = len(v_competidores)
    print('IMPORTANTE. No pueden ser nombres repetidos.')
    print('Ingresar a continuación los datos de los competidores.')

    for i in range(n):
        nom = validar_nombre(v_competidores)
        cont = validar_continente()
        rank = validar_ranking()

        # asignamos a la posicion el registro con los datos correspondientes
        v_competidores[i] = Competidor(nom, cont, rank)


# esta función selecciona un nombre del vector
def nombre_aleatorio(nom_op):
    nomb = random.choice(nom_op)

    # lo retira de la lista, asegurando que no se repita.
    nom_op.remove(nomb)

    return nomb


def carga_automatica(v_competidores):
    n = len(v_competidores)

    # creamos un vector con nombres posibles
    nombres = ['Buffy', 'William', 'Xander', 'Willow', 'Anya', 'Angel', 'Cordelia', 'Giles',
               'Tara', 'Daniel', 'Meredith', 'Derek', 'Cristina', 'Isabel', 'Alex',
               'George', 'Miranda', 'Richard', 'Preston', 'Addison', 'Callie', 'Mark',
               'Lexie', 'Andrew', 'Owen', 'Arizona', 'April', 'Jackson',
               'Link', 'Amelia']

    # recorre el vector para cargar los datos
    for i in range(n):
        # generamos datos aleatorios
        nom = nombre_aleatorio(nombres)
        cont = random.randint(0, 4)
        rank = random.randint(1, 150)

        # asignamos a la posicion el registro con los datos correspondientes
        v_competidores[i] = Competidor(nom, cont, rank)


def carga_competidores(v_competidores):

    # ingresa modo de carga de datos y asegura que sea válido
    modo_carga = validar_tipo_carga()

    # inicia carga de datos según lo elegido, si deja vacío continúa
    # en automático por defecto
    if modo_carga in 'aA':
        carga_automatica(v_competidores)

    else:
        carga_manual(v_competidores)
