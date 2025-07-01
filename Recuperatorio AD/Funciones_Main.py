#1
def mostrar_estudiantes(estudiantes:list, notas:list) -> list:
    for i in range(len(estudiantes)):
        print(f"{estudiantes[i]} -> {notas[i]}")

#2
def sacar_promedio(estudiantes:list, notas:list) -> list:
    datos = []

    for i in range(len(estudiantes)):
        total = 0
        for nota in notas[i]:
            total += nota
        promedio = total / len(notas[i])
        datos.append([estudiantes[i], promedio, notas[i]])

    return datos

def ordenar_promedio(datos:list) -> list:
    for i in range(len(datos)-1):
        for j in range(i+1, len(datos)):
            if datos[i][1] < datos[j][1]:
                aux = datos[i]
                datos[i] = datos[j]
                datos[j] = aux

    return datos

#3
def encontrar_alumno(estudiantes: list, nombre: str) -> int:
    """Busca un alumno y retorna su posición. Si no existe, retorna -1."""
    posicion = -1  
    for i in range(len(estudiantes)):
        if estudiantes[i] == nombre:
            posicion = i 
            break  
    return posicion  

def mostrar_calificaciones(estudiantes: list, notas: list, nombre: str):
    posicion = encontrar_alumno(estudiantes, nombre)
    if posicion != -1:
        print(f"{nombre} -> {notas[posicion]}")
    else:
        print(f"No se encontró a {nombre}.")

#4

def buscar_por_calificacion(notas:list, estudiantes:list, materias:list, calificacion:int):
    encontrado = False
    for i in range(len(estudiantes)):
        for j in range(len(materias)):
            if notas[i][j] == calificacion:
                print(f"Nota encontrada: {calificacion}, Estudiante: {estudiantes[i]}, Materia: {materias[j]}")
                encontrado = True
                
    if not encontrado:
        print("No se ha encontrado a ningún estudiante con esta calificación.")

                
