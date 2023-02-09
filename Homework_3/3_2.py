text = input('Введите текст: ')
result = {key: text.count(key) for key in set(text)}
print(result)
