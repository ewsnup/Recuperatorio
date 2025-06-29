#Gestión de Calificaciones de Estudiantes con Lista/Array y Matriz en Python

# Lista Estudiantes
estudiantes = ["Ana", "Bruno", "Carla", "Diego"]
materias = ["Matemática", "Historia", "Biología"]
notas = [
    [9, 8 , 10],
    [6, 7, 8],
    [10, 10, 9],
    [7, 6, 5]
]

from Funciones_Main import *

abrir = True
while abrir:
    print("\nBienvenido al menú de opciones:")
    print("1. Mostrar estudiantes y sus calificaciónes.")
    print("2. Ordenar estudiantes por promedio.")
    print("3. Buscar estudiante por nombre.")
    print("4. Buscar estudiantes y materia por calificación.")
    print("5. Salir.")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        print("")
        mostrar_estudiantes(estudiantes, notas)
    elif opcion == "2":
        print("")
        print("Ordenando por promedio de notas...")
        datos = sacar_promedio(estudiantes, notas)
        datos_ordenados = ordenar_promedio(datos)
        for estudiante in datos_ordenados:
            print(f"{estudiante[0]}: {estudiante[1]} -> {estudiante[2]}")
    elif opcion == "3":
        print("")
        nombre = input("Ingrese el nombre del estudiante que desea buscar: ")
        print(f"\nBuscando a {nombre}...")
        mostrar_calificaciones(estudiantes, notas, nombre)
    elif opcion == "4":
        print("")
        calificacion = int(input("Ingrese la calificación: "))
        resultado = buscar_por_calificacion(notas, estudiantes, materias, calificacion)
        if resultado == False:
            print("No se ha encontrado a ningún estudiante con esta calificación.")
    elif opcion == "5":
        print("\nSaliendo del programa...\n")
        abrir = False
    else:
        print("Opción invalida. Intente de vuelta.")