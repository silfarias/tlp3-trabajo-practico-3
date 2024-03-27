def missing_number(n, numbers):
    return (n*(n+1)//2) - sum(numbers)



# assert missing_number(5, [1, 2, 3, 4, 5]) == 3, "Error en el caso de prueba"
print(missing_number(6, [1, 2, 3, 4, 6]))