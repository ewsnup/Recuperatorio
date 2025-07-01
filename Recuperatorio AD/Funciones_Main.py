#1
def mostrar_estudiantes(estudiantes:list, notas:list):
    '''
    Muestra a cada estudiantes y sus notas correspondientes.
    '''
    for i in range(len(estudiantes)):
        print(f"{estudiantes[i]} -> {notas[i]}")

#2
def sacar_promedio(estudiantes:list, notas:list) -> list:
    '''
    Calcula el promedio de notas para cada estudiante y devuelve una lista.
    '''
    datos = []

    for i in range(len(estudiantes)):
        total = 0
        for nota in notas[i]:
            total += nota
        promedio = total / len(notas[i])
        datos.append([estudiantes[i], promedio, notas[i]])

    return datos

def ordenar_promedio(datos:list) -> list:
    '''
    Ordena la lista de estudiantes por promedio (de mayor a menor)
    usando bubble sort.
    '''
    for i in range(len(datos)-1):
        for j in range(i+1, len(datos)):
            if datos[i][1] < datos[j][1]:
                aux = datos[i]
                datos[i] = datos[j]
                datos[j] = aux

    return datos

#3
def encontrar_alumno(estudiantes: list, nombre: str) -> int:
    '''
    Busca un estudiante por nombre y devuelve su índice (o -1 si no existe).
    '''
    posicion = -1  
    for i in range(len(estudiantes)):
        if estudiantes[i] == nombre:
            posicion = i 
            break  
    return posicion  

def mostrar_calificaciones(estudiantes: list, notas: list, nombre: str):
    '''
    Muestra las notas y el nombre del estudiante si existe.
    '''
    posicion = encontrar_alumno(estudiantes, nombre)
    if posicion != -1:
        print(f"{nombre} -> {notas[posicion]}")
    else:
        print(f"No se encontró a {nombre}.")

#4

def buscar_por_calificacion(notas:list, estudiantes:list, materias:list, calificacion:int):
    '''
    Busca estudiantes que tengan una calificación específica
    en alguna materia y muestra las coincidencias.
    '''
    encontrado = False
    for i in range(len(estudiantes)):
        for j in range(len(materias)):
            if notas[i][j] == calificacion:
                print(f"Nota encontrada: {calificacion}, Estudiante: {estudiantes[i]}, Materia: {materias[j]}")
                encontrado = True

    if encontrado == False:
        print("No se ha encontrado a ningún estudiante con esta calificación.")

                
