# Definimos la función para verificar si el usuario ingresado es válido...
def validar_usuario(usuario):
    car_anterior = None
    arroba = 0

    # Revisamos que el primer y último caracter del dominio no sean "."
    # o "@". Si alguna de las condiciones se cumple, no es correcto
    # el dominio y devuelve False...
    if usuario[0] == "." or usuario[-1] == ".":
        return False
    elif usuario[0] == "@" or usuario[-1] == "@":
        return False

    # Revisamos la cantidad de arrobas y puntos seguidos...
    for car in usuario:
        if car == "@":
            arroba += 1

        if car_anterior == "." and car == ".":
            return  False

        car_anterior = car

    if arroba != 1:
        return False

    #Retorna True si no se detectó ningún error.
    return True

# definimos la función que verificara el máximo de intentos disponibles...

def verificar_intentos (usuario):
    usuario_ok = False
    vueltas = 0
    while vueltas < 3 and not usuario_ok:

        if vueltas !=0:

            print("\n*~ Hubo un error en los datos cargados. ~*\n")
            usuario = input("Reingrese el usuario: ")

        usuario_ok = validar_usuario(usuario)
        vueltas += 1

    return usuario_ok

# Esta función determina cuales de las regiones no tienen casos
# y devuelve un string con el resultado.

def reg_sin_casos(pri,seg,ter,cua):
    if pri == 0 or seg == 0 or ter == 0 or cua == 0:

        res_pri = res_seg = res_ter = res_cua = ""

        if pri == 0:
            res_pri = "Capital. "

        if seg == 0:
            res_seg = "Gran Córdoba. "

        if ter == 0:
            res_ter = "Norte. "

        if cua == 0:
            res_cua = "Sur. "

        res = res_pri+res_seg+res_ter+res_cua

    else:

        res = ""

    return res

# Definimos la función para el cálculo y redondeo de los promedios.
def promedio (acum, cont):
    if cont != 0:
        res = round(acum / cont)
    else:
        res = -1

    return res

# Definimos la función para el cálculo y redondeo de los porcentajes...
def porcentaje (cont1, cont2):
    if cont2 != 0:
        res = round(cont1 * 100 / cont2,2)
    else:
        res = -1

    return res

# Definimos las funciones que muestran los resultados solicitados...
def mostrar_casos_positivos (contador, porcent):
    if contador != 0:
        print("\nLa cantidad de casos confirmados es: ", contador, "y el porcentaje "
              "\nsobre el total de casos es: ", porcent, "%")
    else:
        print("\nNo hay casos con resultado positivo para evaluar.")
    return

# Definimos las funciones que muestran los resultados segun cada opción del menú...
def mostrar_casos_edad_riesgo(promed):
    if promed != -1:
        print("\nLa edad promedio de los pacientes que pertenecen"
              "\nal grupo de riesgo es: ", promed, "años.")

    else:
        print("\nNo hay casos que pertenezcan al grupo de riesgo.")

    return


def mostrar_casos_salud(contador, porcent):
    if porcent != -1:
        print("\nLa cantidad de casos que pertenecen al personal de salud es: ", contador,
          "\ny el porcentaje que representa es: ", porcent,"%.")

    else:
        print("\nNo hay casos que pertenezcan al personal de salud.")

    return


def mostrar_edad_promedio_positivos(promed):
    if promed != -1:
        print("\nLa edad promedio entre los casos confirmados es: ", promed, " años.")

    else:
            print("\nNo hay casos positivos de COVID-19.")

    return

def mostrar_menor_autoctono(edad):
    if edad > 0:
        print("\nEl paciente de menor edad entre los casos "
              "\autóctonos tiene: ", edad, " años.")

    else:
        print("\nNo hay casos autóctonos para evaluar")

    return

def mostrar_region(region, contador, porcent):
    if contador != 0:
        print("\nLa cantidad de casos confirmados en la región",
              region, "\nes ", contador , " y representa el ", porcent, "%.")

    else:
        print("\nNo hay casos en la región ", region, " para evaluar.")

    return

def mostrar_casos_exterior(contador):
    if contador != 0:
        print("\nLa cantidad de casos confirmados con viaje al exterior es: ", contador)

    else:
        print("\nNo hay casos con viaje al exterior.")

    return

def mostrar_casos_contacto(contador):
    if contador != 0:
        print("\nLa cantidad de casos sospechosos en contacto con casos confirmados es: ", contador)
    else:
        print("\nNo hay pacientes que hayan tenido contacto con casos positivos.")

    return

def mostrar_regiones_sin_casos(regiones):
    if regiones:
        print("\nLas regiones sin casos confirmados son: ", regiones)
    else:
        print("\nNo hay regiones sin casos positivos.")

    return

def mostrar_autoctonos(porcent):
    if porcent > 0:
        print("\nEl porcentaje de casos positivos autóctonos es de ", porcent, "%.")
    else:
        print("\nNo hay casos autóctonos para evaluar.")

    return

# Definimos la función principal.

def main ():
    import random

    # Bienvenida al programa e instrucciones para el usuario….
    print("* "*38)
    print("\t Bienvenido al Programa para Generación de Estadísticas de COVID-19.")
    print("* "*38)
    print("\nDeberá utilizar una cuenta de usuario en el formato nombre@dominio.\n"
          "Por favor, tener en consideración que el mismo no debe comenzar o\n"
          "terminar con puntos ‘.’ o arrobas ‘@’, contar con dos o más puntos\n"
          "seguidos ‘..’ ni más de un arroba.\n")

    # Comenzamos con la primera parte de la carga de datos…

    usuario = input("Ingrese su usuario: ")

    # Verificamos que el usuario se haya ingresado correctamente y no supere la cantidad de intentos…
    usuario_ok = verificar_intentos(usuario)

    if usuario_ok:

        # Carga del número de pacientes y verificamos que se ingrese una cantidad válida…
        n = int (input("\nIngrese la cantidad de pacientes que desea procesar: "))

        while n < 1:
            print("\n","* "*38)
            print("\t\tNo se puede procesar su solicitud.")
            print(" *"*38)

            n = int (input("\nPor favor, ingrese nuevamente la cantidad de pacientes"
                 "\nque desea procesar: "))

        # Declaramos contadores necesarios…
        positivo_cont = exterior_cont = contacto_cont = salud_cont = 0
        edad_positivo_acum = edad_riesgo_acum = riesgo_cont = 0
        autoctono_menor = autoctono_cont = 0
        capital_cont = gran_cont = norte_cont = sur_cont = 0

        edad_ant = 100

        for i in range(n):

            edad = random.randint(1,99)

            # Si el número es 1 consideramos positiva la respuesta…
            res_pos = random.randint(0,1) == 1

            # Creamos la tupla que contiene las regiones posibles…
            regiones = ["cap", "gran", "norte", "sur"]
            region = random.choice(regiones)
            contacto = random.randint(0,1) == 1

            # Consideramos que es improbable que exista personal de salud menores de edad…
            salud = edad >= 18 and random.randint(0,1) == 1
            exterior = random.randint(0,1) == 1

            # Filtramos los resultados positivos para generar…
            if res_pos:
                positivo_cont +=1
                edad_positivo_acum += edad

                # Validamos si es autóctono y de serlo contamos cuantos casos lo son…
                if not (contacto or salud or exterior):
                    autoctono_cont +=1

                    # Buscamos la menor edad entre los autóctonos…
                    if edad < edad_ant:
                        autoctono_menor = edad

                # Determinamos a que región pertenece y contabilizamos…
                if region == "cap":
                    capital_cont += 1
                elif region == "gran":
                    gran_cont += 1
                elif region == "norte":
                    norte_cont += 1
                elif region == "sur":
                    sur_cont += 1

                # Contamos los casos confirmados que hayan tenido un viaje al exterior…
                if exterior:
                    exterior_cont += 1

            # Los pacientes con resultado negativo mayores de 60 componen el grupo de riesgo…
            elif edad > 60:
                edad_riesgo_acum += edad
                riesgo_cont += 1

            # Contamos los casos con contacto con positivos y los que son personal de salud…
            if contacto:
                contacto_cont += 1

            if salud:
                salud_cont += 1

            edad_ant = edad

        # Realizamos los cálculos necesarios..
        pos_porcent = porcentaje(positivo_cont, n)
        sal_porcent = porcentaje(salud_cont, n)

        riesgo_prom = promedio(edad_riesgo_acum,riesgo_cont)

        pos_prom = promedio(edad_positivo_acum, positivo_cont)
        cap_porcent = porcentaje(capital_cont, positivo_cont)
        nor_porcent = porcentaje(norte_cont, positivo_cont)
        sur_porcent = porcentaje(sur_cont, positivo_cont)
        gran_porcent = porcentaje(gran_cont, positivo_cont)
        aut_porcent = porcentaje(autoctono_cont, positivo_cont)

        regiones_sin_casos = reg_sin_casos(capital_cont,gran_cont,norte_cont,sur_cont)

        # Declaramos la variable y comenzamos el menú de opciones
        opcion = 1

        while opcion != 0:
            # Visualización de las opciones…
            print("\nOpciones:")
            print(" 1. Cantidad de confirmados y su porcentaje sobre el total.")
            print(" 2. Promedio de edad de los pacientes del grupo de riesgo.")
            print(" 3. Cantidad del personal de salud y el porcentaje que tienen sobre el total.")
            print(" 4. Promedio de la edad de casos confirmados.")
            print(" 5. Menor edad entre los casos autóctonos.")
            print(" 6. Cantidad de confirmados por región y el porcentaje de cada una sobre el total.")
            print(" 7. Cantidad de casos confirmados que realizaron un viaje al exterior.")
            print(" 8. Cantidad de pacientes sospechosos que tuvieron contacto con confirmados.")
            print(" 9. Regiones sin casos confirmados.")
            print("10. Porcentaje de los casos autóctonos sobre el total de positivos.")
            print(" 0. Salir\n")

            opcion = int(input("Ingrese el número de la la opción elegida: "))

            if 0 <= opcion <=10:
                if opcion == 1:
                    mostrar_casos_positivos(positivo_cont, pos_porcent)

                elif opcion == 2:
                    mostrar_casos_edad_riesgo(riesgo_prom)

                elif opcion == 3:
                    mostrar_casos_salud(salud_cont,sal_porcent)

                elif opcion == 4:
                    mostrar_edad_promedio_positivos(pos_prom)

                elif opcion == 5:
                    mostrar_menor_autoctono(autoctono_menor)

                elif opcion == 6:
                    mostrar_region("Capital", capital_cont, cap_porcent)
                    mostrar_region("Gran Córdoba", gran_cont, gran_porcent)
                    mostrar_region("Norte", norte_cont, nor_porcent)
                    mostrar_region("Sur", sur_cont, sur_porcent)

                elif opcion == 7:
                    mostrar_casos_exterior(exterior_cont)

                elif opcion == 8:
                    mostrar_casos_contacto(contacto_cont)

                elif opcion == 9:
                    mostrar_regiones_sin_casos(regiones_sin_casos)

                elif opcion == 10:
                    mostrar_autoctonos(aut_porcent)

            else:
                print("\nReintente. La opción ingresada no es válida.")

    else:
        print("\n*~ Ha excedido la cantidad de intentos. ~* ")

    print("\n","* "*25)
    print("\t\tGracias por utilizar este programa.")
    print(" *"*25)

    return

main()
