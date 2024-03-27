# Weird Algorithm

n = int(input("Ingrese un número: "))

def weird_algorithm (n):

    secuencia = [n] # Inicializamos la secuencia

    while n != 1: # Repetimos la secuencia con las restricciones
        if n % 2 == 0:
            # Si n es par lo dividimos por 2
            n //= 2 
        else:
            n = n * 3 + 1 # Si no lo multiplicamos por 3 y le sumamos 1
        secuencia.append(n) # Agregamos el nuevo valor

    return secuencia

# Caso de prueba
assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Secuencia incorrecta"
print("Secuencia correcta")

print(weird_algorithm(n))
