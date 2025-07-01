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

from Funciones_main import *

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
            print("")
            mostrar_estudiantes(estudiantes, notas)
        case "2":
            print("")
            print("Ordenando por promedio de notas...")
            datos = sacar_promedio(estudiantes, notas)
            datos_ordenados = ordenar_promedio(datos)
            for estudiante in datos_ordenados:
                print(f"{estudiante[0]}: {estudiante[1]} -> {estudiante[2]}")
        case "3":
            print("")
            nombre = input("Ingrese el nombre del estudiante que desea buscar: ")
            print(f"\nBuscando a {nombre}...")
            mostrar_calificaciones(estudiantes, notas, nombre)
        case "4":
            print("")
            calificacion = int(input("Ingrese la calificación: "))
            resultado = buscar_por_calificacion(notas, estudiantes, materias, calificacion)
            if resultado False:
                print("No se ha encontrado a ningún estudiante con esta calificación.")
        case "5":
            print("\nSaliendo del programa...\n")
            abrir = False
        case _:
            print("Opción invalida. Intente de vuelta.")
