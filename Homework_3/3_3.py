n = int(input('Размер словаря(n): '))

#result = {x: {i: input(f"Введите имя+адрес в количестве {n}: ") for i in ['name', 'email']} for x in range(n)}
result = {x: {'name': input("Введите имя: "), 'email': input("Введите адрес: ")} for x in range(n)}
print(result)