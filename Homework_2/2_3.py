first_name = input('Введите имя: ')
age = int(input('Введите возраст: '))
city = input('Введите город: ')
# Вариант 1
input("Хай, меня зовут "+ first_name+", мне "+age+", я из "+city)

# Вариант 2
#input("Хай, меня зовут %s, мне %d, я из %s" % (first_name, age, city))

# Вариант 3
#input("Хай, меня зовут {}, мне {}, я из {}".format(first_name, age, city))
