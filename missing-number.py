def missing_number(n, numbers):
    return (n * (n + 1) // 2 ) - sum(numbers)

print(missing_number(9, [1, 2, 3, 4, 5, 6, 7, 9]))