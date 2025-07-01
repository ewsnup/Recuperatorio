# ->

temperaturas = [18, 22, 25, 20, 21]
umbral = 20

def temperatura_media_alta(temperaturas:list, umbral:int) -> bool: #Pasa por parametro la lista temperaturas y el umbral que es un entero. Retorna un booleano.
    '''
    Saca el promedio de las temperaturas de la lista y si el promedio
    es mayor al umbral retorna True. Caso contrario retorna False.
    '''
    total = 0
    flag = False
    
    for temperatura in temperaturas:
        total += temperatura
        promedio = total / len(temperaturas)
        if promedio > umbral:
            flag = True
    return flag

print(temperatura_media_alta(temperaturas, umbral))
# Se llama a la función y printea True



