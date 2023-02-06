text = input('Введите предложение: ')
words = text.split()
words[-1], words[0] = words[0], words[-1]
print(' '.join(words))
