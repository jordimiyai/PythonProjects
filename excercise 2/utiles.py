# pausa el desarrollo del programa para facilitar la comprensión
def pausar():
    input('{:^80}'.format('- '*5 + 'Presione ENTER para continuar' + ' -'*5))
    print()


# validamos el método de carga elegido por el usuario
def validar_tipo_carga():
    print()
    tipo = input('Ingrese el método de carga de datos. A- Automático. M- Manual. ')

    # ingresa al ciclo si la opción ingresada no es correcta si no se ingresa
    # opción se deja por default en automático
    while tipo not in 'amAM' and tipo != '':
        tipo = input('Error. Ingrese una opción válida: ')

    print()
    return tipo
