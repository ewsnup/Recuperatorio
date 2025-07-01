#Gestión de Calificaciones de Estudiantes con Lista/Array y Matriz en Python
from Funciones_Main import *
from Listas import *

abrir = True
while abrir:
    print("""\nBienvenido al menú de opciones:
1. Mostrar estudiantes y sus calificaciónes.
2. Ordenar estudiantes por promedio.
3. Buscar estudiante por nombre.
4. Buscar estudiantes y materia por calificación.
5. Salir.""")

    opcion = input("\nSeleccione una opción: ")
    
    match opcion:
        case "1":
            print()
            mostrar_estudiantes(estudiantes, notas)
        case "2":
            print("\nOrdenando por promedio de notas...")
            datos = sacar_promedio(estudiantes, notas)
            datos_ordenados = ordenar_promedio(datos)
            for estudiante in datos_ordenados:
                print(f"{estudiante[0]}: {estudiante[1]} -> {estudiante[2]}")
        case "3":
            nombre = input("\nIngrese el nombre del estudiante que desea buscar: ")
            print(f"\nBuscando a {nombre}...")
            mostrar_calificaciones(estudiantes, notas, nombre)
        case "4":
            try:
                calificacion = int(input("\nIngrese la calificación: "))
                resultado = buscar_por_calificacion(notas, estudiantes, materias, calificacion)
            except ValueError:
                print("Ingreso inválido. Solo ingresar números.")
        case "5":
            print("\nSaliendo del programa...\n")
            abrir = False
        case _:
            print("Opción invalida. Intente de vuelta.")
