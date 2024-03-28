# Missing Number

def missing_number(n, lista):

    suma_total = 0 # Inicializamos la suma total de la secuencia, de 1 hasta n

    # Calculamos la suma de la secuencia 
    for i in range(1, n + 1): # Recorremos la lista de 1 hasta n
        suma_total  += i # Sumamos el valor de la lista

    suma_lista = sum(lista)
    return suma_total - suma_lista # Retornamos la suma total de la secuencia menos la suma de la lista

# Caso de prueba
assert missing_number(9, [1, 2, 3, 4, 5, 6, 7, 9]) == 8, "Error en la suma de la secuencia"
print("Secuencia correcta")

print(missing_number(7, [1, 2, 3, 4, 6, 7]))