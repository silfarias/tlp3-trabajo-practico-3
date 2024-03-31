# Palindrome Reorder

def palindrome_reorder(s):
    repet = {} # Inicializamos un diccionario vacío
    for i in s: # Recorremos la cadena
        if i in repet:
            repet[i] += 1 # Si i ya esta en el diccionario, incrementamos el valor
        else:
            repet[i] = 1 # Si no, le agregamos el valor 1

    conteo_impar = sum(1
                       for i in repet.values() # Recorremos los valores del diccionario
                       if i % 2 != 0) # Verificamos si hay un valor impar

    if conteo_impar > 1:
        return "NO SOLUTION" # Si hay mas de un valor impar, retornamos "NO SOLUTION"
        
    palindrome = '' # Inicializamos una cadena vacía 
    mitad = '' # Mitad del palindromo: caracter impar

    for i, j in repet.items(): # Iteramos sobre los elementos del diccionario
        if j % 2 == 0: # Si la frecuncia del caracter es par

            # i es el caracter y j // 2 es la frecuencia
            palindrome += i * (j // 2) # Cada caracter se agregará la mitad de veces 
        else:
            mitad = i # Si la frecuencia es impar, guardamos el caracter en 'mitad'

    # Retornanmos la mitad del palindrome original, el caracter del centro y el reverso
    return palindrome + mitad + palindrome[::-1]

assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"
print("Todos los casos de prueba han pasado correctamente")