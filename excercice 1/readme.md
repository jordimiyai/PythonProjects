Programa para Generación de Estadísticas de COVID-19 (Coronavirus)
En el contexto de la pandemia de COVID-19, se solicita desarrollar un programa que permita generar estadísticas sobre pacientes sospechosos, a los cuales se les ha realizado el test (o hisopado) de COVID-19 y a partir del mismo se genera información de utilidad para la toma de decisiones en nuestra Provincia.
En primer lugar, el sistema debe solicitar la cuenta de usuario de la persona que generará el reporte. La cuenta debe ingresarse con formato nombre@dominio y el programa validará que cumpla con las siguientes reglas:
•	Tener un sólo caracter @ en una posición intermedia de la cadena (ni la primera ni la última letra)
•	No contener dos puntos seguidos (uno a continuación del otro)
•	No empezar ni terminar con un punto
Si la cuenta ingresada es inválida, se debe permitir el reingreso de la misma. Luego de tres intentos incorrectos, el programa debe detener la ejecución.
Luego de confirmar que la cuenta es válida, solicitar al usuario que ingrese la cantidad de pacientes a procesar. Y a continuación, por cada paciente sospechoso, generar de manera aleatoria los siguientes datos:
•	Edad
•	Resultado del test (Positivo/Negativo)
•	Región (Capital, Gran Córdoba, Norte y Sur)
•	Si tuvo contacto con casos confirmados
•	Si es personal de salud
•	Si viajo al exterior
El programa automáticamente determinará si se considera un caso autóctono. Se considera un caso autóctono si el resultado del test fue positivo y NO estuvo en contacto con casos confirmados, NO es personal de salud y NO viajó al exterior.
Una vez cargados y procesados los datos de los n pacientes, mediante un menú de opciones, informar:
1.	Cantidad de casos confirmados (test positivo) y porcentaje sobre el total de casos.
2.	Edad promedio de los pacientes que pertenecen a grupo de riesgo (para pertenecer al grupo de riesgo el test debe ser negativo y tener más de 60 años).
3.  Cantidad y porcentaje que el personal de salud representa sobre el total de casos
4.	Edad promedio entre los casos confirmados.
5.	Menor edad entre los casos autóctonos.
6.	Cantidad de casos confirmados por región y porcentaje que representa cada uno sobre el total de casos.
7.	Cantidad de casos confirmados con viaje al exterior.
8.	Cantidad de casos sospechosos en contacto con casos confirmados.
9.	Las regiones sin casos confirmados.
10.	Porcentaje de casos positivos autóctonos sobre el total de positivos.
